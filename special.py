class Employee:
    
    raise_amount = 1.04

    def __init__(self, first, last, pay):
    ## __init__ is the special method. "__" - The double underscore is dunder
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return f'{self.first}{self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
    ##This is also special method(__repr__) or magic method or dunder method

        return f'{self.first}{self.last}{self.pay}'

    def __str__(self):
    #This is also next magic/dunder/special method
        return f'{self.fullname()} {self.email}'


emp_1 = Employee('Pukar', 'Thakuri', 30000)
emp_2 = Employee('Subha', 'Pokharel', 300000)

print(emp_1.__repr__())
print(emp_1.__str__())