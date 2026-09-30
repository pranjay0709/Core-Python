class Shape:
    def execute(self):
        print('Area given')
    def validate(self):
        print('area')
class Rectangle(Shape):
    pass

c=Rectangle()
print(c.execute())