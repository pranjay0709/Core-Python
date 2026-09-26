class person:
    def __init__(self):
        self.name = " "
        self.address = " "
        self.age = 0

    def setname(self,name):
        self.name = name

    def setaddress(self, address):
        self.address = address

    def setage(self, age):
        self.age = age
    def getname(self):
        return self.name
    def getaddress(self):
        return self.address
    def getage(self):
        return self.age


p = person()
p.setname('PJ')
p.setaddress('indore')
p.setage(18)
print(p.getname())
print(p.getage())
print(p.getaddress())