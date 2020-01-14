class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
       

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property
    def fullname(self):
        #This is the method that defines full names

        return f'{self.first}{self.last}'


@fullname.setter
def fullname(self,name):
    first, last = name.split(' ')
    self.first = first
    self.last = last

emp_1 = Employee('John', 'Smith') 
##This is the instance having different parameters

emp_1.fullname = 'Bibhuti Chaulagain'

emp_1.first = 'Jim'
print(emp_1.fullname)
#fullname() is a method so we need to add '()' after fulllname like we added in emp1.fullname()
#But, if we add @property above full name, there's no need to add '()'

print(emp_1.email)
#Since email method has @property i.e. getter and setter. So, we do not add '()'


