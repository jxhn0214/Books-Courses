from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten(".,!@?") == ".,!@?"
    assert shorten("6767") == "6767"
    assert shorten("AEIOUx") == "x"