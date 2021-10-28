# if

a = 10

if a == 10:
    print('test 1 true')
else:
    print('test 1 false')

if a >= 0 and a <=10 :
    print('test 2 true')

if a >= 0 or a <=10 :
    print('test 3 true')

if a != 10:
    print('test 4 false')


keys = ['a', 'b', 'c']

if 'a' in keys:
    print('test 5 true')
if 'a' not in keys:
    print('test 5 false')

if 'a' in keys:
    print('test 6 a')
elif 'b' in keys:
    print('test 5 b')
elif 'c' in keys:
    print('test 5 c')
