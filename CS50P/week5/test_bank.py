from bank import value
import pytest


def test_value():
    assert value("Hello") == 0
    assert value("hey, what's up") == 20
    assert value("What's up, I havent seen you in a while.") == 100
