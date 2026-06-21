from um import count


def test_basic_um():
    assert count("um") == 1


def test_um_case_insensitive():
    # should still count even if caps
    assert count("Um, thanks") == 1
    assert count("UM, hello, um") == 2


def test_um_not_substring():
    # "yummy" and "album" have "um" in them but shouldnt count
    assert count("yummy") == 0
    assert count("Um, thanks for the album.") == 1


def test_multiple_ums():
    assert count("Um, thanks, um...") == 2
    assert count("um um um") == 3


def test_no_um():
    # no um at all
    result = count("hello world")
    assert result == 0