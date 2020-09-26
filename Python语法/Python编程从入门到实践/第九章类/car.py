class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 设置默认值

    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print("odometer:"+str(self.odometer_reading))

    def update_odometer(self,mileage): # 直接修改属性值
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("不能回调里程计")
        
    def increment_odometer(self,miles): # 在原来的基础上增加值
        self.odometer_reading += miles
    
'''
my_new_car = Car('audi','a4',1998)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(24)
my_new_car.read_odometer()
my_new_car.update_odometer(12)
my_new_car.odometer_reading = -100
my_new_car.read_odometer()
'''

# 9.3 子类和继承
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        # 创建子类独有的方法和属性
        self.battery_size = 70
    def describe_battery(self):
        print("battery size"+str(self.battery_size))
'''
my_tesla = ElectricCar('Tesla','model s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
'''

# 9.3.5 类的嵌套

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("Battery size"+str(self.battery_size))

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        # 创建子类独有的方法和属性
        self.battery = Battery()

my_tesla = ElectricCar('Tesla','model s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()