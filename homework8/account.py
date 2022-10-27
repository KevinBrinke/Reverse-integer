#Kevin Brinke r01423368
#account class


class Account:
    def __init__(self):
        self.__id= 0  # identification, initial balance, annual interest rate
        self.__ib= 100.00
        self.__air= 0.00

    def setID(self,idnumber):
        if idnumber > 0 : #positive number
            if len(str(idnumber))==4:#id of 4 digits long
                self.__id = idnumber
        else:
            print("not a valid ID number")    
    
    def getID(self):
        return self.__id

    def setBalance(self,balance):
        if balance >=0 :
            self.__ib=balance

    def getBalance(self):
        return self.__ib

    def setAIR(self, annualInterestRate):
        if annualInterestRate >=0 :
            self.__air= annualInterestRate

    def getAIR(self):
        return self.__air
#took the /100 out because i printed a percentage symbol for the rates return values not actual value
    def getMIR(self):
        return self.__air / 12


    def getMI(self):
        return (self.__air /100 / 12)* self.__ib

    def withdraw(self,wAmount):
        if self.__ib >= wAmount>0:  #withdraw has to be lower than available balance
            print("Withdrew $",wAmount,"out of your loan account")

            self.__ib = self.__ib - wAmount
            return self.__ib
        else:
            print(wAmount,"is not a valid withdrawal")
    

    def deposit(self,dAmount):
        
        if dAmount>0:
            print("Deposited $",dAmount,"into your loan account")
            self.__ib = self.__ib + dAmount
            return self.__ib + dAmount
        
        else:
            print(dAmount,"is not a valid deposit")


