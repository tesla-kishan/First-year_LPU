#polymorphism with inheritance
class bird:
  def intro(self):
    print("hii this is a bird class")
  def flight(self):
    print("most of the bird can fly")
class parrot(bird):
  def flight(self):
    print("parrot can fly")
class ostrich(bird):
  def flight(self):
    print("ostrich cannot fly")
obj1=bird()
obj2=parrot()
obj3=ostrich()

obj1.intro()
obj1.flight()

obj2.intro()
obj2.flight()

obj3.intro()
obj3.flight()