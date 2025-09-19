for value in range (1, 5):
    print(value)

for value in range(10, 15):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)


squares = []

for value in range(1,10):
    square = value ** 2
    squares.append(square)

print(squares)

for value in range(1,6):
    squares.append(value**2)

print(squares)

print(min(squares))

print(max(squares))
print(sum(squares))