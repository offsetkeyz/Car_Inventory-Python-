from Car import *


class CarList:

    def __init__(self, date, list_of_cars):

        # the date acts as the name of the list
        self.date = date
        self.list_of_cars = list_of_cars

    def find_car(self, stock_number):
        for car in self.list_of_cars:
            if type(car) is Car:
                if stock_number == car.stock_number:
                    return f"{car} was shot on {self.date}" # TODO maybe make this boolean
            else:
                return "This is not a car"
        return "Stock number not found"

    # Returns all cars in list to String
    def __str__(self) -> str:
        blurb = ""
        for car in self.list_of_cars:
            blurb += car.__str__() + "\n"
        return blurb
