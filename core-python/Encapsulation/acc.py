class account:
    def __init__(self):
        self.acc_no = 0
        self.acc_balance = 0
        self.acc_type = 0
        self.deposit_count = 0
        self.withdrawl_count = 0

    def setacc_no(self, acc_no):
        self.acc_no = acc_no

    def setacc_balance(self, acc_balance):
        self.acc_balance = acc_balance

    def setacc_type(self, acc_type):
        self.acc_type = acc_type

    def getacc_no(self):
        return self.acc_no

    def getacc_balance(self):
        return self.acc_balance

    def getacc_type(self):
        return self.acc_type

    def withdrawl(self, amt):
        if amt > self.acc_balance:
            print('insufficent balance')
        elif amt>50000:
            print('You do not have limit to withdraw 50k')
        else:
            self.withdrawl_count>5
            self.withdrawl_count+=1
            self.acc_balance = self.acc_balance - amt
            print('Your withdrawl remains:', 5 - self.withdrawl_count)
            print('Your Acc_balance is:', self.acc_balance)

    def deposit(self, amt):
        if amt > 100000:
            print('You cannot deposit more than 1Lakh')
        else:
            self.deposit_count > 10
            self.acc_balance += amt
            self.deposit_count += 1
            print('Your Acc_balance is:', self.acc_balance)
            print('Your deposit remains:', 10 - self.deposit_count)



p = account()
p.setacc_no(45412554)
p.setacc_balance(1423)
p.deposit(90000)
p.deposit(255)
print(p.getacc_no())
print(p.getacc_balance())
p.withdrawl(5000)
