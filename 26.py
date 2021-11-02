#input

name = input("Please enter your name:")
print("Hello " + name)

age = input("How old are you?")
age = int(age) #default input is recorded as string, use int() to transfer to int type
if age >= 18:
    print("adult")
else:
    print("kid")
