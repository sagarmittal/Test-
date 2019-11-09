class Employee:
    num_of_employee = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_employee += 1

    # this is an instance method. Needs an instance of the object to work
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    # this is a class method, it needs a class to act upon
    # we can also use by using the instance of the object to call the object
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str: str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    # this is a static method. It doesn't need an instance or class
    # but still somehow its connected to the class
    # its better to make static method than to use a regular method
    @staticmethod
    def is_workday(date):
        if date.weekday()==5 or date.weekday()==6:
            return False
        return True


class Developer(Employee):
    # Here the method resolution order is set to ->
    # Developer -> Employee -> builtins.objects
    # Every class in python inherits from builtins.objects
    # we can see this by writing help(Developer)

