
user = {
    'root': 123456,
    'alice': 'alice123',
    'bruce': 'brc123',
}

for k, v in user.items():
    print("username:" + k + ',' + 'password:' + str(v))


for k in user.keys():
    print(k)

if 'admin' not in user.keys():
    print('key: admin not exist!')

for v in user.values():
    print(str(v))

for k in sorted(user.keys()):
    print(k)

user['cindy'] = 123456

for v in set(user.values()):
    print(str(v))