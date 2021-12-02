class Dog():
    # constructor，'self' is similar to C++ 'this' pointer
    # Unlike C++, all member data is defined in __init__
    def __init__(self, name, age, place=""):
        self.name = name
        self.age = age
        self.place = place # set by input or default value

    # method of the class, 'self' must be passed in as explicit argument.
    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll(self):
        print(self.name.title() + " rolled over!")
    
    def set_place(self, place):
        self.place = place


mydog = Dog('willie', 5)

print(mydog.name, mydog.age, mydog.place)
mydog.sit()
mydog.roll()

mydog.set_place("home")
print(mydog.place)