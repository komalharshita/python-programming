#helloworld

print("Hello, World!")

#number

num = float(input())

if num > 0 :
  print("The number is positive")
elif num < 0 :
  print("The number is negative")
else :
  print("The number is positive")
  
#leapyear
  
year = int(input())

if ( year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
  print(f"{year} is a leap year!")
else : 
  print(f"{year} is not leap year")

#gradecalc

marks = int(input("Enter your marks: "))

if marks >= 90 :
  print("Grade: A")
elif marks >= 80 and marks < 90 :
  print("Grade: B")
elif marks >= 70 and marks < 80 :
  print("Grade: C")
elif marks >= 60 and marks < 70 :
  print("Grade: D")
else :
  print("  Fail")
  
#divisibleby5and3

number = int (input())

if ( number % 3 == 0 and number % 5 == 0) :
  print("The number is divisible by 3 and 5")
else :
  print("The number is not divisible by 3 and 5")
  
#smallestofthree

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if (n1 < n2 and n1 < n3):
  print(f"{n1} is the smallest of three")
elif (n2 < n1 and n2 < n3):
  print(f"{n2} is the smallest of three")
else : 
  print(f"{n3} is the smallest of three")
  
#vowelorcons

char = input("Enter a character: ").lower()

if char in 'aeiou' :
  print(f"{char} is a vowel")
else : 
  print(f"{char} is a consonant")
  
#oddoreven

oddeven = int(input("Enter a number : "))

if (oddeven % 2 == 0):
  print(f"{oddeven} is even. ")
else:
  print(f"{oddeven} is odd. ")
  
#validityoftriangle

side1 = int(input())
side2 = int(input())
side3 = int(input())

if ( side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2):
  print("The triangle is valid!")
else : 
  print("The triangle is invalid")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  