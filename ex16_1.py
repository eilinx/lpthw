# -*- coding:utf-8 -*-

from sys import argv

script, filename = argv

print("I'm going to load one file and attend some context in file {}.".format(
    filename))

target = open(filename, 'w+')

line1 = raw_input('line1: ')
line2 = raw_input('line2: ')
line3 = raw_input('line3: ')

target.write("{0}\n{1}\n{2}\n".format(line1, line2, line3))
print("Ok {} is updated.".format(filename))

target.close()
