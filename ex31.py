# -*- coding:utf-8 -*-

print("You enter a dart room with two doors. Do you go through #1 or #2?")
door = input("> ")

if door == 1:
    print("There's a biant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")
    if bear == 1:
        print("The bear eats your face off. Good Job.")
    elif bear == 2:
        print("The bear eats your legs off. Good Job.")
    else:
        print("Well, doing {} is probably better. Bear runs away.".format(bear))

elif door == 2:
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insannity = input("> ")
    if insannity == 1 and insannity == 2:
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insannity rots your eyes into a pool of muck. Good Job.")

else:
    print("You stumple around and fall on a knife an die. Good Job ! ")