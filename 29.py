#function

def greeting():
    print("hello")

greeting()


def greeting(username):
    print("hello " + username)

greeting('alice')


#default parameter value
def describe_pet(pet_name, animal_type='dog'):
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('willie') #implicit assign parameter
#describe_pet(pet_name='willie') #explicit assign parameter


#return value
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

name = get_formatted_name('jimi', 'hendrix')
print(name)