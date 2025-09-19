alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [ alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] == 'yellow'
        alien['speed']== 'medium'
        alien['points'] == 10

for alien in aliens[:5]:
    print(alien)
print("....")

print(f"Total number of aliens: {len(aliens)}")

alien_0 = {'color': 'green' , 'points' : 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!\n")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print(f"\nThe alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

print(alien_0)

del alien_0['points']
print(alien_0)