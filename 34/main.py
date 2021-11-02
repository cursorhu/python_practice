#import specific functions:
#from module_name import function_name 

#import all functions: (not recommend because imported module function may have same name with current program)
#from module_name import *

from pizza import make_pizza

#no need to use pizza.make_pizza for this case.
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')