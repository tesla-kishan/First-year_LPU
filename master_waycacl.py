#simple calculator
#user defined fn
def add(x,y):
  return x+y
def subtract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def divide(x,y):
  return x/y

print("select the given option")
print("1. Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=input("choose 1/2/3/4:")


num1=float(input("Enter 1st number:"))
num2=float(input("Enter 2nd number:"))

if choice =="1":
  print(add(num1,num2))
elif choice=="2":
  print(subtract(num1,num2))
elif choice=="3":
  print(multiply(num1,num2))
elif choice=="4":
  print(divide(num1,num2))

else:
  print("choose correctly")