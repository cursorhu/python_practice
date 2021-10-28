# Use range and list to fast create an number array.

for value in range(1,6):
    print(value)

numbers = list(range(1,6))
print(numbers)


numbers = []
for n in list(range(1, 11)):
    v = 2 ** n
    numbers.append(v)

print(numbers)