# Importing array library 

import array

# Creating an array

arr = array.array("f", (1.0, 1.5, 2.0, 2.5))
print(arr[1])

# Arrays are mutable:

arr[1] = 23.0
print(arr)

#appending items

arr.append(42.0)
print(arr)
arr[1] = "hello"
print(arr)

#deleting an arry

del arr[1]
print(arr)