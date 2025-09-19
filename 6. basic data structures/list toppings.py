requested_topping = "mushrooms"

if requested_topping != "anchovies" :
    print("Hold the anchovies!")

requested_toppings = [ 'mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

if 'mushrooms' in requested_toppings :
    print("Adding mushrooms")
if 'pepperoni' not in requested_toppings :
    print("Adding pepperoni")
if 'extra cheese' not in requested_toppings:
    print("Adding extra cheese")

print(requested_toppings)
print("\nFinished making your pizza!")

requested_toppings = [ 'mushrooms', 'green peppers', 'extra cheese']
print(requested_toppings)

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers!")
    else :
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")

print(requested_toppings)

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings :
        print("Adding {requested_topping}")
    print("\nFinished making your pizza!")
else :
    print("Are you sure you want a plain pizza?")

print(requested_toppings)

print('Available toppings: ')
available_toppings = [ 'mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
print(available_toppings)

print('Requested toppings: ')
requested_toppings = [ 'mushrooms', 'french fries', 'extra cheese']
print(requested_toppings)

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry! we dont have {requested_topping}")
print("\nFinished making your pizza!")





