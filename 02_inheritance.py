# create a class with car brand and model and add subclass 

class Car:  #class

    def __init__(self,brand,model): #constructor
        self.brand=brand
        self.model=model

    def get_car_info(self):  # method
        print(f"car model is {self.model} and car brand is {self.brand}")


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
         
        super().__init__(brand,model) # super()--> To get constructor / method Property
        self.battery_size=battery_size
    
    def get_car_info(self):
        print(super().get_car_info(),f" Baterry Size is {self.battery_size}")

my_car=Car("Tata","Safari") # class object 'Car'
my_car.get_car_info()

my_new_car=ElectricCar("Tesla","Model s","85kWh") #subclass object 'ElectricCar'
my_new_car.get_car_info()
