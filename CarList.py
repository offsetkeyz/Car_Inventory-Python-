from Car import *


class CarList:

    def __init__(self, list_of_cars):

        self.list_of_cars = list_of_cars

    def find_car(self, stock_number):
        for car in self.list_of_cars:
            if type(car) is Car:
                if stock_number == car.stock_number:
                    return car
            else:
                return "This is not a car"
        return "Stock number not found"
