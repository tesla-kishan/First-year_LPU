#check prime or not 
count = 0
n = int(input('Enter number to check : '))
i = 2
while i <= (n/2):
    if (n%i) == 0:
        count = 1
        break
if n == 1:
    print('1 is not prime')
elif count == 0:
    print(n,' is a prime number.')
elif count == 1:
    print(n,' is not a prime number.')