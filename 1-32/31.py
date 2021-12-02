#use list in function

def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

def edit_users1(names):
    for name in names:
        name = ''

def edit_users2(target_names, src_names):
    for name in src_names:
        target_names.append(name)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#not work
edit_users1(usernames)
print(usernames)

#works
new_usernames = []
edit_users2(new_usernames, usernames)
print(new_usernames)

#not work, put in a slice copy but not original list.
new_usernames2 = []
edit_users2(new_usernames2[:], usernames)
print(new_usernames2)