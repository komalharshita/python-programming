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
