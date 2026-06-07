from bank import value


#
def test_hello():
    assert value("HELLO") == 0
    assert value("hello") == 0
    assert value("Hello sir") == 0


#
def test_h_greetings():
    assert value("Hi") == 20
    assert value("How are you") == 20
    assert value("Halleluyah") == 20


#
def test_other_greetings():
    assert value("Wagwan") == 100
    assert value("Good Morning") == 100
    assert value("01") == 100
