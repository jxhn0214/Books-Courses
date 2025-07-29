import fuel
import pytest


def test_convert():
    assert fuel.convert("1/4") == 25
    assert fuel.convert("3/4") == 75
    assert fuel.convert("2/3") == 67


def test_gauge():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(25) == "25%"
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")


def test_negative_divison():
    with pytest.raises(ValueError):
        fuel.convert("-1/1")
    with pytest.raises(ValueError):
        fuel.convert("1/-1")