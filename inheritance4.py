class animal:
  def speak(self):
    print("animal is speaking")
class dog(animal):
  def bark(self):
    print("dog barking")
class puppy(dog):
  def eat(self):
    print("cat is eating break")
a=puppy()
a.speak()
a.bark()
a.eat()