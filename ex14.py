# -*- coding:utf-8 -*-

from sys import argv
script, user_name, lover_name = argv
prompt = "> "

print("Hi, {0}, I, lover_name'm the {1} script".format(user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me {}?".format(user_name))
likes = raw_input(prompt)
print(likes)

print("Where do you live {}?".format(user_name))
lives = str(raw_input(prompt))

print("What kind of computer do you have?")
computer = str(raw_input(prompt))

print("""
Alright, so you said {0} about likeing me.
you live in {1}, Not sure where that is.
And you have a {2} computer. Nice.
And you like {3}.

""".format(likes, lives, computer, lover_name))
