# -*- coding:utf-8 -*-

# this one is like your script with argv


def print_two(*args):
    arg1, arg2, arg3 = args
    print("arg1: {}, arg2: {}, arg3: {}".format(arg1, arg2, arg3))

# ok, that *args is actually pointless, we can just do this


def print_two_again(arg1, arg2):
    print("arg1: {}, arg2: {}".format(arg1, arg2))


def print_one(arg1):
    print("arg1: {}".format(arg1))


def print_none():
    print("I got nothing")

print_two('Zed', 'Shaw', 'leo')
print_two_again('Zed', 'Shaw')
print_one('First')
print_none()
