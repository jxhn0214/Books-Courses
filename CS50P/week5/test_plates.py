from plates import is_valid
import pytest


def test_is_valid():
    assert is_valid("1234") == False
    assert is_valid("ABCDEFGHIJK") == False
    assert is_valid("AB12DE") == False
    assert is_valid("ABC01") == False
    assert is_valid("ABC-12") == False

