#array operations

bicycles = ['trek', 'cannondale', 'redline']
bicycles.append('specialized')
print(bicycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motor = motorcycles.pop()
print(motor)
print(motorcycles)

motor = motorcycles.pop(0)
print(motor)
print(motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)