#map

alien = {'color': 'green', 'points': 5}
print(alien['color'])
print(alien['points'])


alien['position_x'] = 0
alien['position_y'] = 10
print(alien)

alien['color'] = 'blue'
print(alien)

del alien['color']
print(alien)