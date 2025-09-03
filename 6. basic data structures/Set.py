# Creating a Set 

Set = set([1, 2, 'fairy', 4, 'For', 6, 'mermaid']) 
print("\nSet with the use of Mixed Values") 
print(Set) 

# Accessing element using for loop 

print("\nElements of set: ") 
for i in Set: 
    print(i, end =" ") 
print()

# Checking the element using in keyword 
print("fairy" in Set)

normal_set = set(["a", "b","c"])
print("Normal Set")
print(normal_set)

# A frozen set

frozen_set = frozenset(["e", "f", "g"])

print("\nFrozen Set")
print(frozen_set)
