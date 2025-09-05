# program to print table of a number 

num = int(input("Enter any number: "))
print("format 1: ")

for i in range(1, 11):
    print(num*i)
print()

print("format 2: ")

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

