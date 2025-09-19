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
