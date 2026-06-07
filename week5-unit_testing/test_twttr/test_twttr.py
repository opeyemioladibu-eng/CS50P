from twttr import shorten


# Test that Uppercase vowels are omitted
def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("OLADIBU") ==  "LDB"


# Test that lower case vowels are omitted
def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("oladibu") == "ldb"


# Test that numbers are not affected
def test_numbers():
    assert shorten("132twitter") == "132twttr"
    assert shorten("oladibucs50p") == "ldbcs50p"


#Test that punctuation marks are not affected
def test_punctuation():
    assert shorten("Hello, CS50P") == "Hll, CS50P"
    assert shorten("....oladibu....") == "....ldb...."
