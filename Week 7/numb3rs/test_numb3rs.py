from numb3rs import validate

def test_string():
    assert validate("cat") == False
def test_range():
    assert validate("192.512.512.512") == False
def test_octets():
    assert validate("255.192.128.128.192") == False
