from hello import more_hello, more_goodbye


def test_hello():
    assert "hi" == more_hello()


def test_bye():
    assert "bye" == more_goodbye()
