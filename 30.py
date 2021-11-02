#optional parameter

def get_formatted_name1(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

name = get_formatted_name1('john', 'lee', 'hooker')
print(name)

# the optional parameter must set at last place
def get_formatted_name2(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

name = get_formatted_name2('jimi', 'hendrix')
print(name)
name = get_formatted_name2('john', 'hooker', 'lee')
print(name)