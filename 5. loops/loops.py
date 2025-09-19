print("Hello, World!")

#primenumber

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
  
#typeoftriangle

a = int(input())
b = int(input())
c = int(input())

if ( a == b == c):
  print("Equilateral triangle")
elif ( a == b or b == c or c == a):
  print("Isosceles triangle")
else :
  print( "Scalene triangle")





















