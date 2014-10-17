# -*- coding:utf-8 -*-

name = 'Zed A. Shaw'
age = 35  # not a lie
weight = 180  # lbs
height = 74  # inch
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about {0}".format(name))
print("He's {0} inches tall".format(height))
print("He's {0} pounds heavy.".format(weight))
print("Actually that's not too heavy")
print("He's got {0} eyes and {1} hair.".format(eyes, hair))
print("His teeth are usally {0} depending on the coffee.".format(teeth))
# This line is tricky, try to get it right.
print("If i add {0}, {1} and {2} I get {3}".format(
    age, height, weight, (age + weight + height)))
