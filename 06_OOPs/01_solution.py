class Car:
    total_car = 0

    def __init__(self, brand, model) :
        self.brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.brand + " !"

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of land transport"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))

print(my_tesla.model)
print(my_tesla.fuel_type())
print(my_tesla.get_brand())
print(my_tesla.full_name())

my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)
print(my_new_car.fuel_type())

print(Car.total_car)

print(Car.general_description())



class Battery:
    def battery_info(self):
        return "This is Battery"

class Engine:
    def engine_info(self):
        return "This is Engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())