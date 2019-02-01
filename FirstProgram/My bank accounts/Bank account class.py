#Matthew Walker
#1/17

class Bank_acc(object):


    def __init__(self,name):
        self.account_num = [123,124,125]
        self.phone_num = input("enter your phone number")
        self.pin_num = 123456
        self.balance = 38
        self.name = name

    def deposit(self,balance):
        ammount = int(input("how much are you depositing"))
        self.balance += ammount
        print(balance)


    def withdraw(self,balance,account_opt):
        ammount = int(input("how much are you withdrawing?"))
        self.balance += ammount
        print("balance")
        account_opt(mAcc.withdraw,mAcc.deposit)

    def enter_account(self,account_num,account_opt,pin_num,enter_account,withdraw,deposit):
        user_acc = int(input("what is your account num?"))
        if user_acc in account_num:
            user_acc = int(input("what is your pin"))
            if user_acc == pin_num:
                account_opt(withdraw,deposit)
        else:
            print("thats not an account number")
            enter_account()





        input("what is your pin?")
    def account_opt(self,withdraw,deposit):
        choose = input("press d to deposit w to withdraw or s to see current amount")
        if choose == "w":
            withdraw(mAcc.balance,mAcc.account_opt)
        elif choose == "d":
            deposit(mAcc.balance,mAcc.account_opt)

mAcc = Bank_acc("Matthew")
mAcc.enter_account(mAcc.account_num,mAcc.account_opt,mAcc.pin_num,mAcc.enter_account,mAcc.withdraw,mAcc.deposit)
