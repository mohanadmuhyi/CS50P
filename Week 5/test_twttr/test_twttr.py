from twttr import shorten

def test_upper():
    assert shorten("TWITTER") == "TWTTR"
def test_lower():
    assert shorten("twitter") == "twttr"
def test_numbers():
    assert shorten("Twitter100") != "Twttr"
def test_punc():
    assert shorten("Good, Twitter") != "Gd Twttr"
