import masscan

import workers.utils.domain2ip as domain2ip


class MassScan:
    def __init__(self, targets, ports=None):
        self.targets = " ".join(targets)
        self.ports = ports

        self.masscan_arguments = " --max-rate 1000"

    def run(self):
        try:
            mas = masscan.PortScanner()
            mas.scan(hosts=self.targets, ports=self.ports, arguments=self.masscan_arguments)
            host_results = []
            print(mas.scan_result)
            for host in mas.all_hosts:
                port_results = []
                for proto in mas[host]:
                    for port in mas[host][proto]:
                        port_results.append({
                            "port": port,
                            "service_name": mas[host][proto][port]['services'],
                            "protocol": proto
                        })
                host_results.append({
                    "ip": host,
                    "port_info": port_results,
                    "os_info": None
                })
            return host_results, None
        except masscan.PortScannerError as e:
            return None, e


if __name__ == '__main__':
    ips = "github.com,114.114.114.114"
    task = MassScan(domain2ip.convert(ips), "22,80,8080,30000,53")
    result, err = task.run()
    if err is not None:
        print(err)
    else:
        print(result)
