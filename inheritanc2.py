class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def display(self):
    print(self.name,self.age)
class employee(person):
  def __init__(self,name,age):
    person.__init__(self,name,age)
a=employee("kishan",20)
a.display()