#Kevin Brinke R01423368


#ok so i realize now that i didnt really need a class for this assignment but i already made it 
class PasswordCheck:
    def __init__(self):
        self.__password= "no password created"
        
    def setPassword(self,passwordSet):
        numberCount=0#how many numbers are in the password, must >=2
        invalid=3#subtracts 1 if any of the rules are broken, if not 3 it will produce false
        wrongChar=False #just to tell wrong characters were used
        
        
        if len(passwordSet) < 7:#rule 1
            invalid -= 1
            print("Not long enough")
            
            
        for i in range (len(passwordSet)):#rule 2
            if 48 <= ord(passwordSet[i]) <= 57 or 65<=ord(passwordSet[i])<=90 or 97<=ord(passwordSet[i])<=122 :
                
                if passwordSet[i].isdigit(): 
                    numberCount+=1
            else:
                wrongChar=True                
        if wrongChar:
            print( "Wrong characters used")       
            invalid -=1
       

        if numberCount<2:#rule 3
            print("Must have more number characters\nYou have:",numberCount,"numbers\nNeeds at least 2")
            invalid -= 1
        
        if invalid==3:#wanted outcome
            self.__password= passwordSet
            return True

    def getPassword(self):#i know this wasnt needed, but already created it
        return self.__password
            



def main():
    account= PasswordCheck()
    
    passCheck=False
    while passCheck is False:#keeps asking for password if rules were not followed
        userInput=input("Enter a password with the following conditions:\n\t1.Must be at least 8 characters\n\t2.Must consist of only digits and letters\n\t3.Must contain at least 2 digits\n\nNew Password: ")
       

        if account.setPassword(userInput) is True:
            passCheck = True
        
    
        print(account.getPassword())

main()