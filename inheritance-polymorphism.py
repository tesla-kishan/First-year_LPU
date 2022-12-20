class India():
  def capital(self):
    print("NEW DELHI is the capital of India")
  def language(self):
    print("many languages are spoken in india")
class USA():
  def capital(self):
    print("Washington DC is the capital of America")
  def language(self):
    print("England is the primary language spoken")

def test(obj):
  obj.capital()
  obj.language()

obj1=India()
obj2=USA()

test(obj1)
test(obj2)
