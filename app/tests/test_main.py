from .config import client


def test_ping(client):
    res = client.get("/ping")
    assert res.status_code == 200
