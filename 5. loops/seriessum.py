import math

# series type - 1 + x/1! + x^2/ 2! +...... x^n/n!

n = int(input("Enter number of terms: "))
x = int(input("Enter the base: "))

s = 1

for i in range(1, n+1):
    s = s + math.pow(x, i) / math.factorial(i)
print(s)


# series type - 