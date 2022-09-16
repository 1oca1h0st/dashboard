import pytest
import workers.assets.scan as scan


def test_nmap_scan():
    targets = ["github.com"]
    ports = "443"
    task = scan.NmapScan(targets=targets, ports=ports)
    result, err = task.run()
    print(result)
    assert err is None
