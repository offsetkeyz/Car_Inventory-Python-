from Car import *
from CarList import *

firstList = [Car("P3456", "Findlay", "Honda", "Accord", 2020, 15, "new"),
             Car("P3446", "Findlay", "Honda", "Accord", 2020, 15, "new"),
             Car("P3457", "Findlay", "Honda", "Accord", 2020, 15, "new")]

actual_list = CarList("Dec 7, 1941", firstList)
list_two = CarList("Dec 6, 2020", firstList)

list_of_lists = [actual_list, list_two]
for l in list_of_lists:
    print(l.find_car("P3456"))

print(list_of_lists)

print(actual_list.find_car("P3445"))
print(actual_list)
