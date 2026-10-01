class Shape:
    def execute(self):
         if self.validate():
            self.area()
         else:
             print('Validation failed')

    def validate(self):
            return False
    def area(self):
        print("Shape area")

class Rectangle(Shape):
    def __init__(self,L,W):
        self.length=L
        self.width=W
    def validate(self):
        if self.length>0 and self.width>0:
            return True
        else:
            return False


    def area(self):
        rectangle_area =self.length*self.width
        print("Area_of_rectangle", rectangle_area)
        return rectangle_area

class Circle(Shape):
    PI=3.14
    def __init__(self, R):
        self.radius = R

    def validate(self):
            if self.radius > 0:
                return True
            else:
                return False

    def area(self):
        circle_area = self.PI*self.radius*self.radius
        print("Area_of_circle", circle_area)
        return circle_area

c = Circle(5)

c.execute()
r=Rectangle(5,4)
r.execute()

r2=Rectangle(-1,5)
r2.execute()