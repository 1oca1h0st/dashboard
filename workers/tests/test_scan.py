import workers.assets.scan as scan

targets = ["github.com"]
ports = "443"


def test_nmap_scan():
    task = scan.NmapScan(targets=targets, ports=ports)
    result, err = task.run()
    print(result)
    assert err is None
