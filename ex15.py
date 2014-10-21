# -*- coding:utf-8 -*-

# import sys.argv to get argument.
from sys import argv

# assign argument to variable.
script, filename = argv

# open file which is from cmd
txt = open(filename)
# print message.
print("Here's your file {}.".format(filename))
# type all context of files.
print(txt.read())
# close file`
txt.close()

print("Type the filename again:")
file_again = raw_input('> ')
txt_again = open(file_again)
print(txt_again.read())
txt.close()
