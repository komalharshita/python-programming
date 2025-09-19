import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())

coefficients = [ a, b, c, d]

roots = np.roots(coefficients)

print(f"The roots are {roots}")