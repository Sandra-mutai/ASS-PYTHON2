class Account:
    def __init__(self,name,phone,account,loan_limit) :
        self.name=name
        self.phone=phone
        self.account=account
        self.balance=0
        self.loan=0
        self.loan_limit=loan_limit
   

    # def show(self,balance):
    #     return self.balance

    def deposit(self,amount):
        if amount <=0:
            return f"the amount must be grater than zero"
        else:
            self.balance +=amount
            return f"dear {self.name} you have deposited KES {amount} your new balance is {self.balance}"

    def withdraw(self,amount):
        if amount <=0:
            return "the amount must be grater than zero"
        elif (amount<self.balance):
            return "the amount must be less than the balance"
        else:
            self.balance+=amount
            return f"amount reduces the balance"

    def borrow(self,amount):
        if amount<=self.loan_limit:
            return f"you are above your loan limit"
        elif self.loan>0:
            return f"you cant borrow loan"
        else:
            self.loan+=1
            self.balance+=amount
            return f"you have successfully borrow your loan"



