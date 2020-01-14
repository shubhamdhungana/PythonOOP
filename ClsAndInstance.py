#Python OOP


# ###########usual way############################
# class Employee:
#     pass

# emp_1 = Employee()
# emp_2 = Employee()

# print(emp_1)
# print(emp_2)

# emp_1.first = "shubham"
# emp_1.last = "Dhungana"
# emp_1.email = "shubhamdhungana01117@gmail.com"
# emp_1.pay = 39,0000

# emp_2.first = "Subha"
# emp_2.last = "Dhungana"
# emp_2.email = "subha@gmail.com"
# emp_2.pay = 59,0000

# print(emp_1.email)
# print(emp_2.email)







##############OOP Way##################################p
class Employee:

    def __init__(self, first, last, pay):
       

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
    ##fullname() is the method         
        return f'{self.first} {self.last}'

    def email(self):
        ###This is email() method
        return


emp_1 = Employee('Shubham', 'Dhungana', 40000) ##instance
emp_2 = Employee('Subha', 'Pokhrel', 90000)


# print(emp_1.email)
# print(emp_2.email)


print(emp_2.fullname())
print(Employee.fullname(emp_1))

print(" ")
print(emp_2.email)






