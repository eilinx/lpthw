# -*- coding:utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


# this first kind of for-loop ges through a list.

for number in the_count:
    print("This is count {}.".format(number))

# same as above

for fruit in fruits:
    print("A fruit of type: {}.".format(fruit))

# also we can go through mixed lists too.
# notice we have to use r% since we don't know what's in it.
for i in change:
    print("I got {}.".format(i))

# we can also build lists, first start with an empty one
elements = []

# then use the range functions to do 0 to 5 counts

for i in range(0, 6):
    print("Adding {}, to elements list.".format(i))
    elements.append(i)

# now we can print them out too.

for i in elements:
    print("Elements was {}.".format(i))

elements_2 = range(0, 6)
print(elements_2)