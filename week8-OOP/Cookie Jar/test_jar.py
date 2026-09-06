import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_init_custom_capacity():
    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

def test_init_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("12")
    with pytest.raises(ValueError):
        Jar(12.5)

def test_deposit():
    jar = Jar(10)
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(4)
    assert jar.size == 7

def test_deposit_over_capacity():
    jar = Jar(5)
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.deposit(1)
    assert jar.size == 5

def test_withdraw():
    jar = Jar(10)
    jar.deposit(7)
    jar.withdraw(3)
    assert jar.size == 4

def test_withdraw_too_many():
    jar = Jar(5)
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.withdraw(4)
    assert jar.size == 3

def test_str():
    jar = Jar(10)
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪🍪"
