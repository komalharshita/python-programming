# ARITHMETIC OPERATORS
a = 15
b = 4

print("Addition:", a + b)  
print("Subtraction:", a - b) 
print("Multiplication:", a * b)  
print("Division:", a / b) 
print("Floor Division:", a // b)  
print("Modulus:", a % b) 
print("Exponentiation:", a ** b)

# COMPARISON OPERATORS
a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

#LOGICAL OPERATORS
a = True
b = False
print(a and b)
print(a or b)
print(not a)

#BITWISE OPERATORS
a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

#ASSIGNMENT OPERATORS
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

#IDENTITY OPERATORS
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

#MEMBERSHIP OPERATORS
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

#TERNARY OPERATORS
a, b = 10, 20
min = a if a < b else b

print(min)

#Operator Precedence in Python
expr = 10 + 20 * 30
print(expr)
name = "komal"
age = 19

if name == "komal" or name == "harshita" and age >= 10:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

#Operator Associativity in Python
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)

