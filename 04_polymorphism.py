# create a class with car brand and model and add subclass 

class Car:  #class

    total_Car=0  # class count


    def __init__(self,brand,model): #constructor
        self.brand=brand
        self.model=model
        Car.total_Car+=1  # to count how many class 'Car' used in object

    def get_car_info(self):  # method
        print(f"car model is {self.model} and car brand is {self.brand}")

    def fuel_type(self):  # polym
        print("Diesel & Petrol")


class ElectricCar(Car):

    total_Car=0 
    def __init__(self,brand,model,battery_size):
         
        super().__init__(brand,model) # super()--> To get constructor / method Property
        self.battery_size=battery_size
        ElectricCar.total_Car+=1
    
    def get_car_info(self):
        print(super().get_car_info(),f" Baterry Size is {self.battery_size}")

    def fuel_type(self):  # polymorph
        print("Electric Charge")

my_car=Car("Tata","Safari") # class object 'Car'
my_car.get_car_info()
my_car2=Car("Tata","Nexon") # class object 'Car'
my_car2.get_car_info()
my_car.fuel_type()

print(f"total car are : {Car.total_Car}")


my_new_car=ElectricCar("Tesla","Model s","85kWh") #subclass object 'ElectricCar'
my_new_car.get_car_info()
my_new_car2=ElectricCar("BYD","Model ZX","90kWh") #subclass object 'ElectricCar'
my_new_car2.get_car_info()
my_new_car.fuel_type()

print(f"total Electric car are : {ElectricCar.total_Car}")
