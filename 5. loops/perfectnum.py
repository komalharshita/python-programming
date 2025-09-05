# perfect number is a + integer which is equal to sum of its divisors 

num = int(input("Enter a number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if num == sum:
    print("Number is perfect")
else:
    print("Number is not perfect")