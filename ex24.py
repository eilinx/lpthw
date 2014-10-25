# -*- coding:utf-8 -*-

print("Let's practice enerything.")
print(
    "You\'d need to know \' bout escapes with\
     \\ that do \n newlines and \t tabes.'")

poem = """
\t The lovely world
With logic so firmly planted
can't discern \t the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\t\t where there is none.
"""
print("-----------------------")
print(poem)
print("-----------------------")


five = 10 - 2 + 3 - 6
print("This sould be five : {}".format(five))


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)
print("With a starting point of : {}".format(start_point))
print("We'd have {} beans, {} jars and {} crates.".format(
    beans, jars, crates))
start_point /= 10
print("We can also do that this way:")
print("We'd have {} beans, {} jars and {} crates."
      .format(secret_formula(start_point)[0],
              secret_formula(start_point)[1], secret_formula(start_point)[2]))
