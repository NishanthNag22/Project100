class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        
    def checkBalance(self):
        print("Your balance is 100000")

    def withdrawl(self,amount):
        newAmount = 1000000 - amount
        print("You have withdrawn "+str(amount) +". Your remaining balance is "+ str(newAmount))

def main():
    CardNumber = input("Insert your card number : ")
    pinNumber  = input("Enter your pin number : ")

    newUser =  Atm(CardNumber ,pinNumber)

    print("Choose your activity ")
    print("1. Balance Enquriy  2. Withdrawl")
    activity = int(input("Enter activity number : "))

    if (activity == 1):
        newUser.checkBalance()
    elif (activity == 2):
        amount = int(input("Enter the amount you want to withdraw from your account : "))
        newUser.withdrawl(amount)
    else:
        print("Enter a valid number")
main()