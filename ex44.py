class Parent(object):
    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def alterred(self):
        print("PARENT alterred()")

class Child(Parent):
    def override(self):
        print("CHILD override()")

    def implicit(self):
        print("CHILD implicit()")

    def alterred(self):
        print("CHILD, BEFORE PARENT alterred()")
        super(Child, self).alterred()
        print("CHILD, AFTER PARENT alterred()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.alterred()
son.alterred()