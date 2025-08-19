import pytest
from datetime import date
from seasons import get_dob, calculate_delta

def test_invalid_month():
    with pytest.raises(SystemExit):
        get_dob("2000-13-12")
    with pytest.raises(SystemExit):
        get_dob("1999-500-12")
    with pytest.raises(SystemExit):
        get_dob("1700-0-12")


def test_invalid_day():
    with pytest.raises(SystemExit):
        get_dob("2000-12-200")
    with pytest.raises(SystemExit):
        get_dob("1999-02-30")
    with pytest.raises(SystemExit):
        get_dob("1700-01-0")


def test_delta_calculation():
    assert calculate_delta(date.fromisoformat("2024-08-19"), date.today()) == 525600
    assert calculate_delta(date.fromisoformat("2024-01-01"), date.fromisoformat("2025-01-01")) == 527040
