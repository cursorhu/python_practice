#slice's important use: copy list

a = [1, 2, 3]
b = a  # b is only an alias
b.append(4)
print(a)
print(b)


a = [1, 2, 3]
b = a[:]  # b is a copy of a, all data sliced.
b.append(4)
print(a)
print(b)