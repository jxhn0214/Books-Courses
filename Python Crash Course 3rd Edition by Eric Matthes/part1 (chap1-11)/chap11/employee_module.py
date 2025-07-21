class Employee: 
    """Class that describes what we can do to employees"""

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = int(salary)

    def give_raise(self, salary=5000):
        self.salary += salary