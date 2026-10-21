import pytest
from fuel import convert, gauge


def test_convert():
    """ normal case"""
    assert convert("1/4") is 25
    assert convert("3/4") is 75

    """ X > Y should raise ValueError"""
    with pytest.raises(ValueError):
        convert("3/2")

    """ Y = 0 should raise ZeroDivisionError"""
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    """ non-integer should raise ValueError"""
    with pytest.raises(ValueError):
        convert("x/y")

def test_guage():
    assert gauge(1) == "E"    # empty
    assert gauge (99) == "F"  # Full
    assert gauge(50) == "50%" # middle
    