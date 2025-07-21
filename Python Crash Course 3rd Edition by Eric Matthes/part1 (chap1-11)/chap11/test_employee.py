import pytest
from employee_module import Employee

@pytest.fixture
def employee_0():
    employee_0 = Employee('johny', 'cash', 50000)
    return employee_0

def test_give_default_raise(employee_0):
    employee_0.give_raise()
    assert 55000 == employee_0.salary

def test_give_custom_raise(employee_0):
    employee_0.give_raise(10000)
    assert 60000 == employee_0.salary




