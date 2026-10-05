class student:
    def __init__(self):
        self.name = " "
        self.roll_no = " "
        self.Phy_mark = 0
        self.Chem_mark = 0
        self.Math_mark = 0

    def setname(self, name):
        self.name = name

    def setroll_no(self, roll_no):
        self.roll_no = roll_no

    def setPhy_mark(self, Phy_mark):
        self.Phy_mark = Phy_mark

    def SetChem_mark(self,Chem_mark):
        self.Chem_mark = Chem_mark

    def SetMath_mark(self,Math_mark):
        self.Math_mark = Math_mark

    def getname(self):
        return self.name

    def getroll_no(self):
        return self.roll_no

    def getPhy_mark(self):
        return self.Phy_mark

    def getChem_mark(self):
        return self.Chem_mark

    def getMath_mark(self):
        return self.Math_mark


p = student()
p.setname('PJ')
p.setroll_no('049')
p.setPhy_mark(35)
p.SetMath_mark(45)
p.SetChem_mark(45)

print(p.getname())
print(p.getroll_no())
print(p.getPhy_mark())
print(p.getMath_mark())
print(p.getChem_mark())

