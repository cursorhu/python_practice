
available = ['alice', 'bob', 'cindy']

requested = ['alice', 'bourne', 'cassie']

for r in requested:
    if r in available:
        print(r)
    else:
        print(r + ' not available!')