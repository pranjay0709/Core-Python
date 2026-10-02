from abc import ABC, abstractmethod


class Shape(ABC):

    def test(self):
        print("Test Method")

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def area(self):
        print("Rectangle Area Method")

    def test(self):
        print("Rectangle test Method")

r = Rectangle()
r.area()
r.test()
