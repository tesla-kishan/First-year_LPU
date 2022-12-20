num=int(input("Enter no.:"))
count=0
i=2
while i<=num-1:
  if num % i ==0:
    count=count+1
  i=i+1
if count==0:
  print(" prime")
else:
  print(" not prime")