class automobile:
    GEARS = 6

    def __init__(self):
        self.speed = 0
        self.color = " "
        self.name = " "

    def setname(self, name):
        self.name = name

    def setcolor(self, color):
        self.color = color

    def setspeed(self, speed):
        self.speed = speed

    def getname(self):
        return self.name

    def getcolor(self):
        return self.color

    def getspeed(self):
        return self.speed

    def acclerate(self):
        if self.speed >= 450:
            print("Speed limit reached, slow down")
        else:
            self.speed += 10
            print("Your speed is:", self.speed)

    def breaks(self):
        if self.speed == 0:
            print("vehicle is not moving")
        else:
            self.speed -= 10
            print("Your speed is:", self.speed)

    def gear(self, no):
        if no > automobile.GEARS:
            print('invalid gear')

        elif no == 1:
            self.speed = 20
            print('you speed is', self.speed)
        elif no == 2:
            self.speed = 40
            print('you speed is', self.speed)

        elif no == 3:
            self.speed = 60
            print('you speed is', self.speed)
        elif no == 4:
            self.speed = 100
            print('you speed is', self.speed)
        elif no == 5:
            self.speed = 150
            print('you speed is', self.speed)
        elif no == 6:
            self.speed == 400
            print('you speed is', self.speed)


p = automobile()

p.setname('tata')
p.setcolor('red')
# p.setage(18)
p.setspeed(400)
# p.acclerate()
# p.breaks()
p.gear(6)

print(p.getname())
print(p.getcolor())
print(p.getspeed())

# print(p.getaddress())
