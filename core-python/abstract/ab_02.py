from abc import ABC, abstractmethod


class Shape(ABC):

    @classmethod
    def test(cls):
        print("Test Method")

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def area(self):
        print("Rectangle Area Method")


r = Rectangle()
r.area()
Shape.test()
