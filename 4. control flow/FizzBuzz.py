"""
For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz".
"""

# defining the range and adding input

def fizz_buzz(start, end):
    if start > end:
        print("Start should be less than or equal to end.")
        return

    for fizzbuzz in range(start, end + 1):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("FizzBuzz")
        elif fizzbuzz % 3 == 0:
            print("Fizz")
        elif fizzbuzz % 5 == 0:
            print("Buzz")
        else:
            print(fizzbuzz)

print("\nFrom 1 to 10")
fizz_buzz(1, 10)
print("\nFrom 50 to 75")
fizz_buzz(50, 75)


for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("Buzz")
    print(fizzbuzz)