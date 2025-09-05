# This file contains Python code for generating various loop-based patterns.

""" 
A
B C
D E F
G H I J
K L M N O
"""

l = 65
for i in range(1, 6):
    for j in range(1, i+1):
        print(chr(l), end = " ")
        l = l+ 1
    print()

l = 65

""" 
*
**
***
****
*****
"""
print()
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""

n = 5
for i in range(n):
    for j in range(i):
        print('*', end = " ")
    print('')
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end = " ")
    print('')