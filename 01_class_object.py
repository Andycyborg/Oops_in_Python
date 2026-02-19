# create a class with car brand and model

class Car:  #class

    def __init__(self,brand,model): #constructor
        self.brand=brand
        self.model=model

    def get_car_info(self):  # method
        print(f"car model is {self.model} and car brand is {self.brand}")

my_car = Car("tata","safari")  #objectjj

my_car.get_car_info()