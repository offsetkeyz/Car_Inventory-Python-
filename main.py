from Car import *
from CarList import *

firstList = [Car("P3456", "Findlay", "Honda", "Accord", 2020, 15, "new"),
             Car("P3446", "Findlay", "Honda", "Accord", 2020, 15, "new"),
             Car("P3457", "Findlay", "Honda", "Accord", 2020, 15, "new")]

actual_list = CarList(firstList)
print(actual_list.find_car("P3445"))
