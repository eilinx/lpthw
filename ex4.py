# -*- coding: utf-8 -*-

cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are {0} cars available.".format(cars))
print("There are only {0} drivers available.".format(drivers))
print("There will be {0} empty cars today.".format(cars_not_driven))
print("We can transport {0} people today.".format(carpool_capacity))
print("We have {0} to carpool today.".format(carpool_capacity))

print("we need to put about {0} passengers in each car.".format(average_passengers_per_car))
