
# Choose one of below three import method 
# import single class from module
from car import Car
from car import ElectricCar

# import all class
from car import *

# import module only, code must use format 'module.Class', for example, car.Car(), car.ElectricCar()
# import car


# test parent class object 
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# test child class object 
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.odometer_reading = 23
my_tesla.read_odometer()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()