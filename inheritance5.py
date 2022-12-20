class calc1:
  def add(self,a,b):
    return a+b
class calc2:
  def multi(self,a,b):
    return a*b
class calc3(calc1,calc2):
  def div(Self,a,b):
    return a/b
a=calc3()
print(a.add(10,20))
print(a.multi(4,3))
print(a.div(10,5))