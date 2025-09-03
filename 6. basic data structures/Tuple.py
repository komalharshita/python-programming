#creating a tuple

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#printing individual elements

for dimension in dimensions:
    print(dimension)

print("\nOriginal dimensions: ")
for dimension in dimensions:
    print(dimension)

#modifying a tuple 

dimensions = ( 400, 100)
print("\nModified dimensions: ")
for dimesnion in dimensions:
    print(dimension)

#creating a Tuple with the use of Strings

Tuple = ('Hello', 'World')
print("\nTuple with the use of String: ")
print(Tuple)
    
#creating a Tuple with the use of list

list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
Tuple = tuple(list1)
print(Tuple)

#accessing element from last negative indexing

print("\nLast element of tuple")
print(Tuple[-1])
print("\nThird last element of tuple")
print(Tuple[-3])