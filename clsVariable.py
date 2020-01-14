class Employee:
    
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return f'{self.first}{self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Pukar', 'Thakuri', 30000)
emp_2 = Employee('Subha', 'Pokharel', 300000)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(Employee.__dict__)

print(emp_1.pay)
# print(emp_1.apply_raise())
emp_1.raise_amount
print(emp_1.pay)