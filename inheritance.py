#INHERITENCE
class person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def display(self):
    print(self.name,self.age)
class employee(person):
  pass
a=employee("kishan",20)
a.display()