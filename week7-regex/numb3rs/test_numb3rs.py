from numb3rs import validate

def test_valid():
    assert validate("192.168.1.1") is True
    assert validate("0.0.0.0") is True
    assert validate ("255.255.255.255") is True


def test_invalid():
    assert validate("275.3.6.19") is False
    assert validate("ab.de.ef.jkl") is False
    assert validate ("255.1.3") is False
