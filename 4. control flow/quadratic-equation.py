import math

a = int(input())
b = int(input())
c = int(input())

D = b**2 - 4*a*c

if ( D > 0) :
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print(f"The roots are real and distinct. Roots: {root1} and {root2}")

elif ( D == 0 ):
    root = ( -b / ( 2 * a))
    print(f"The roots are real and equal. Roots: {root}")

else :
    print("The roots are complex")