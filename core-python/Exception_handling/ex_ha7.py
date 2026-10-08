class Lg_ex(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Account:
    def __init__(self):
        self.acc_balance = 0

    def setacc_balance(self, acc_balance):
        self.acc_balance = acc_balance

    def getacc_balance(self):
        return self.acc_balance
    def deposit(self, amt):
            self.acc_balance += amt
            print('Your Acc_balance is:', self.acc_balance)

    def withdrawl(self, amt):
        if self.acc_balance-amt>=2000:
            self.acc_balance -= amt
            print(f"Withdrew: {amt}, Remaining Balance: {self.acc_balance}")
        else:
            raise Lg_ex("Insufficient balance. Minimum ₹2000 must remain in the account.")

a =Account()
a.setacc_balance(5000)

try:
    a.deposit(2000)  # balance = 7000
    a.withdrawl(3000)  # balance = 4000
    a.withdrawl(2500)  # will raise exception (balance would go below 2000)
except Lg_ex as e:
    print("exception:", e)

a.deposit(4000)


