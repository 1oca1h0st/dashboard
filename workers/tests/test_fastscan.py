import workers.assets.fastscan as fastscan
import workers.utils.domain2ip as domain2ip

targets = "github.com"
ports = "443"


def test_fastscan():
    task = fastscan.MassScan(targets=domain2ip.convert(targets), ports=ports)
    result, err = task.run()
    assert err is None
