num = int(input("Enter a decimal number: "))

l = []

while (num):
    r = num % 2
    l.append(r)
    num = num // 2

for i in range( len(l) - 1, -1, -1):
    print(l[i], end = " ")