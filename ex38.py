# -*- coding:utf8 -*-

# create a mapping of state

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 20)
print("NY State has: {}.".format(cities['NY']))
print("OR state has: {}.".format(cities['OR']))

# print some states

print('-' * 20)
print("Michigan's abbreviation is:{}".format(states['Michigan']))
print("Florida's abbreviation is :{}".format(states['Florida']))

# do it by using the state then cities dict
print('-' * 20)
print("Michigan has: {}".format(cities[states['Michigan']]))
print("Florida has: {}".format(cities[states['Florida']]))

# print every state abbreviation
print('-' * 20)
for state, abbrev in states.items():
    print("{} has the city {}.".format(state, abbrev))

# print every city  in state
for abbrev, city in cities.items():
    print("{} has the city {}".format(abbrev, city))

# now do both at the same time
print('-' * 20)
for state, abbrev in states.items():
    print("{} state is abbreviated {} and has city {}.".format(
        state, abbrev, cities[abbrev]))

print('-' * 20)
# safely get a abbreviation by state that might not be there
state = states.get('Texax', None)

if not state:
    print("Sorry, no Texas.")

# get a city with a default value.
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is : {}".format(city))
