# string characters printing

for i in "python":
    print(i, end = ' ')
print()

# first 10 even numbers

for i in range(2,22,2):
    print(i, end = ' ')

# first 10 even numbers in reverse order

for i in range(20, 0, -2):
    print(i)

# first 10 odd numbers

for i in range( 1,21,2):
    print(i, end = ' ')

# average of 10 numbers

sum = 0
for i in range(10):
    n = int(input("Enter number: "))
    sum = sum + n
print("Average of these 10 numbers is: ", sum/10)

# elements of a list

mylist = [ 1, 2, 3, 4, 5, 6]
for elements in mylist:
    print(elements)

# product of elements

p = 1
for num in mylist:
    p *= num
print(p)

# number of vowels

name = "komal harshita"
vowels = "aeiouAEIOU"
count = 0
print(name)
for char in name:
    if char in vowels:
        count += 1
print(count)

#listofsquares
num = 1
squares = [ num ** 2 for num in range(1, 6)]
print(squares)