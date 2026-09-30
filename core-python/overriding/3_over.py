class Shape:
    def area(self):
        print("Shape area")

class Rectangle(Shape):
    def __init__(self,L,W):
        self.length=L
        self.width=W

    def area(self):
        rectangle_area =self.length*self.width
        print("Area_of_rectangle", rectangle_area)
        return rectangle_area

class Circle(Shape):
    PI=3.14
    def __init__(self, R):
        self.radius = R

    def area(self):
        circle_area = self.PI*self.radius*self.radius
        print("Area_of_circle", circle_area)
        return circle_area

c = Circle(5)

c.area()
r=Rectangle(5,4)
r.area()