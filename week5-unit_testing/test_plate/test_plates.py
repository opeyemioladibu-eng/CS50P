"""Unit tests for the is_valid function in plates.py"""
from plates import is_valid


def test_len():
    """Test that plates must be between 2 and 6 characters"""
    assert not is_valid("A")         # invalid - too short
    assert is_valid("AB")            # valid - okay length
    assert not is_valid("ABCDEFG")   # invalid - too long


def test_isalpha():
    """Test that the first two characters must be letters"""
    assert is_valid("AA23")       # valid - first two chars are letters
    assert not is_valid("A3A1")   # invalid -- second char is number
    assert not is_valid("22BB")   # invalid - starts with numbers


def test_isalnum():
    """Test that plates may only contain letters and numbers"""
    assert is_valid("AA321")       # valid - only letters and numbers
    assert not is_valid("AA3!2")   # invalid - contains special characters
    assert not is_valid("AA 12")   # invalid - contains whitespace



def test_no_leading_zero():
    """Test that numbers cannot start with zero"""
    assert not is_valid("AA012") # invalid - number started with 0
    assert is_valid("AB102")     # valid - number starts with 1
    assert is_valid("AB202")     # valid - number starts with 2


def test_numbers_at_end():
    """Test that once numbers appear, no letters may follow"""
    assert not is_valid("AA1B2")  # invalid - letter after digit
    assert is_valid("AA12")       # valid - numbers only at the end
    assert not is_valid("AAB1B2") # invalid - letter after digit
