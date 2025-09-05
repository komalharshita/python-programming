# password validity chcker

"""
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""

import re

p = str(input("Enter a password: "))
flag = True

while flag:
    
    if (len(p)< 6 or len(p)> 12):
        print("Password length should be between 6 and 12 characters")
    
    if not re.search("[a-z]" , p):
        print("Password should contain at least one lowercase letter")
       
    
    if not re.search("[0-9]", p):
        print("Password should contain at least one digit")
       
    
    if not re.search("[A-Z]", p):
        print("Password should contain at least one uppercase letter")
     
    
    if not re.search("[$#@]", p):
        print("Password should contain at least one special character")
       
    
    if re.search("\s", p):
        print("Password should not contain any whitespace character")

    else:
        flag = False
        break 


if flag == True:
    print("Valid password")