import nmap


# 部分参考 TophantTechnology/ARL 项目
class NmapScan:
    def __init__(self, targets, ports=None, service_detect=False, os_detect=False, timout=300, port_parallelism=None,
                 max_retries=3, min_rate=64):
        self.targets = " ".join(targets)
        self.ports = ports
        self.min_rate = min_rate
        self.timeout = timout

        self.nmap_arguments = "-sT -n --open"
        self.max_hostgroup = 128
        self.max_retries = max_retries

        # 当出现端口数量较多时，调整nmap的扫描分组以及降低扫描速率
        if len(self.ports.split(",")) > 30000:
            self.max_hostgroup = 8
            self.min_rate = max(self.min_rate, 400)
            self.max_retries = 2

        # 是否识别服务
        if service_detect:
            self.nmap_arguments += " -sV"

        # 识别操作系统
        if os_detect:
            self.nmap_arguments += " -O"

        self.nmap_arguments += " --max-rtt-timeout 800ms"
        self.nmap_arguments += " --max-retries {}".format(self.max_retries)
        self.nmap_arguments += " --min-rate {}".format(self.min_rate)
        self.nmap_arguments += " --script-timeout 6s"
        self.nmap_arguments += " --max-hostgroup {}".format(self.max_hostgroup)
        self.nmap_arguments += " --max-retries {}".format(self.max_retries)
        self.nmap_arguments += " --host-timeout {}s".format(self.timeout)

    def run(self):
        try:
            nm = nmap.PortScanner()
            nm.scan(hosts=self.targets, ports=self.ports, arguments=self.nmap_arguments)
            host_results = []
            for host in nm.all_hosts():
                port_results = []
                for proto in nm[host].all_protocols():
                    for port in nm[host][proto]:
                        info = nm[host][proto][port]
                        result = {
                            "port": port,
                            "service_name": info["name"],
                            "version": info["version"],
                            "product": info["product"],
                            "protocol": proto
                        }
                        port_results.append(result)

                os_info = self.os_match_by_accuracy(nm[host].get("osmatch", []))
                host_results.append({
                    "ip": host,
                    "port_info": port_results,
                    "os_info": os_info
                })

            return host_results, None
        except nmap.PortScannerError as e:
            return None, e

    @staticmethod
    def os_match_by_accuracy(os_match_list):
        for os_match in os_match_list:
            accuracy = os_match.get("accuracy", "0")
            if int(accuracy) > 90:
                return os_match


if __name__ == '__main__':
    task = NmapScan(["github.com"], "22,80,8080", service_detect=True, os_detect=True)
    results, err = task.run()
    if err is not None:
        print(err)
    else:
        print(results)
