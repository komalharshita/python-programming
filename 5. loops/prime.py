# checking prime numbers between two numbers

def primen(num):
  f = 0
  if num == 1 or num == 0:
    f =1
  for i in range(2, num):
    if num% i == 0:
      f = 1
  if f == 1:
    return 'n'
  else:
    return 'y'
  
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"\nPrime numbers between {num1} and {num2} are : ")
if num1>num2:
  for i in range(num2, num1 + 1):
    r = primen(i)
    if r == 'y':
      print(i , end = ' ')
else:
  for i in range(num1, num2 + 1):
    r = primen(i)
    if r == 'y':
      print(i , end = ' ')

# checking indivdual number for prime
print()
print("----Enter a number to check for prime----")
num = int(input())

if (num > 1):
  for i in range (2, int(num**0.5) +1 ):
    if num % i == 0:
      print(f"{num} is not prime number. ")
      break
  else : 
      print(f"{num} is prime number. ")
      
else :
  print(f"{num} is not prime number.")
  






















