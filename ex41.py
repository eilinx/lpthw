# -*- coding:utf-8 -*-

## Animal is a object(yes, sort of confusing) look at th extra credit.

class Animal(object):
    """A New class calls animal"""
    pass

class Dog(Animal):
    """docstring for Dog"""
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    """docstring for Cat"""
    def __init__(self, name):
        self.name = name


class Person(object):
    """docstring for Person"""
    def __init__(self, name):
        
        self.name = name
        self.pet = None


class Emplyee(Person):
    """docstring for Emplyee"""
    def __init__(self, name, salary):
        super(Emplyee, self).__init__(name)
        self.salary = salary


class Fish(object):
    """docstring for Fish"""
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass

## rover is a Dog

rover = Dog('rover')
satan = Cat('Satan')
mary = Person('Mary')

