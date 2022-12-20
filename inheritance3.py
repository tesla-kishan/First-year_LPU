# in class
class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def display(self):
    print(self.name , self.age)

class Employee(Person):
  def __init__(self,name,age,year):
    super().__init__(name,age)
    self.year=year

  def welcome(self):
    print("welcome",self.name,"Ujjwal",self.age,"17","2005",self.year)
a=Employee("Ujjwal",17,2005)
a.welcome()