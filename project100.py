class Atm:
    def __init__ (self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin


    def CashWithdrawl (self, cash):
        print(cash, "$ had withdrawn from your account! ")

    def BalanceEnquiry (self, balance):
        print(" You have ", balance, " left. ")

atm1 = Atm(197038, 1020)
atm1.CashWithdrawl(100)
