from mirrorpulse import run_seed, get_info

def test_smoke():
    out = run_seed({"ping": "pong"})
    assert out.get("ok") is True
    assert "anchors" in out
    info = get_info()
    assert "ethics" in info
