print("Choose an operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

operation = int(input())
n1 = float(input())
n2 = float(input())

if operation == 1:
    print( n1+n2 )
elif operation == 2:
    print( n1 - n2 )
elif operation == 3 :
    print( n1 * n2 )
elif operation == 4 : 
    if n2 == 0 :
        print("Division with zero not allowed")
    else : 
        print( n1/n2 )
elif operation == 5 :
    print( n1 % n2 )
else : 
    print("invalid choice")