from app import greet, add


def test_greet():
    assert greet("Anvash") == "Hello, Anvash! Welcome to GitHub Actions."


def test_add():
    assert add(10, 20) == 30


def test_add_negative_numbers():
    assert add(-5, 5) == 0
