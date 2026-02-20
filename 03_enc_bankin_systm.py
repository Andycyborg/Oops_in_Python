# create a banking system in which we can deposite , withdraw and check balance by encapculating balance anly acces in class not out of class

class Account:  #class

    def __init__(self,balance,name,Ac_No): #constructor

        self.__balance=balance    # encapsulating balance
        self.name=name
        self.Ac_No=Ac_No

    def deposite(self,amount):  #method 
        self.amount=amount

        if amount>0:
            self.__balance+=amount
            print(f"Amount {self.amount} Depoditen in Ac No.:- {self.Ac_No}")

        else:
            print("Invalid Amount")

    def withdraw(self,amount):  #method
        self.amount=amount

        if amount<=self.__balance:
            self.__balance-=amount

            print(f"Withdraw {self.amount} from Ac No.:- {self.Ac_No}")
        
        else:
            print("Invalid Amount")

    def show_balance(self):    # method
        print(f"Ac No. :{self.Ac_No}\nBalance : {self.__balance}")


my_Ac = Account(1000,input("Enter Your Nmae : "), int(input("Enter Your Ac No.: ")))   # object

my_Ac.deposite(500)
my_Ac.withdraw(300)
my_Ac.show_balance()
#print(my_Ac.balance)

