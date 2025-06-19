from jar import Jar

def test_init():
    jar = Jar(5)
    assert jar.capacity == 5

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == ""
