import pytest
from working import convert


def test_both_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_both_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_mixed_formats():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"

def test_overnight():
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_midnight_and_noon():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"