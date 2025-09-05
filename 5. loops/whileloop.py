# product of digits 

p = 1
num = int(input("Enter any two or more digit number: "))
num_p = num 
while(num_p):
    r = num_p % 10
    p = p*r
    num_p = num_p // 10
print("Product of digits is = ", p)

# sum of digits

s = 0
num_s = num
while(num_s):
    u = num_s % 10
    s = s + u
    num_s = num_s // 10
print("Sum of digits is = ", s)