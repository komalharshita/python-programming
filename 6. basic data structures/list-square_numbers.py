
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