#list 1

bicycles = [ 'trek', 'cannodale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

message = f"My first bicycle was {bicycles[1].title()}"
print(message)

#list 2

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

print('Here is the sorted list:')
print(sorted(cars))

cars.reverse()
print(cars)

print(len(cars))

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else :
        print(car.title())

car = 'bmw'
car == 'bmw'
print(car)
car.lower() == 'bmw'
print(car)

#copying a list

myfoods = [ 'pizza', 'biryani', 'burger']
print("My favourite foods: ")
print(myfoods)

friendfoods = myfoods[:]
print("My friends favourite foods: ")
print(friendfoods)

#modyfying lists

motorcycles = [ 'honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.append('bullet')
print(motorcycles)

motorcycles.insert(0, 'honda')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle owned was : {last_owned.title()}")

first_owned = motorcycles.pop(0)
print(f'The first motorcycle owned was: {first_owned.title()}')

motorcycles = [ 'honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.remove('ducati')
print(motorcycles)

