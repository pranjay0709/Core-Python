class Person:
    def address(self):
        print("Default constructor")

p = Person()

print(p.address())


class School:
    def __init__(self):
        print('provided constructor')


a = School()
