# class Employee:
#     num_of_emps = 0
#     raise_amt = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first +'.'+ last + '@gmail.com'
#         self.pay = pay

#         Employee.num_of_emps += 1

#     def fullname(self):
#         return f'{self.first} {self.last}'

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)

#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amt = amount
    


# emp_1 = Employee('Isha', 'Dheke', 50000)
# emp_2 = Employee('Subha', 'Pokharel', 60000)

# # Employee.set_raise_amt(1.05)

# # print(Employee.raise_amt)




