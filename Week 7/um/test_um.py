from um import count

def test_inner():
    assert count("yummy") == 0

def test_beginning():
    assert count("um, hello") == 1

def test_spaces():
    assert count(" um ") == 1

def test_cases():
    assert count("UM") == 1
