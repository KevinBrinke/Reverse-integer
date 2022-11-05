#Kevin Brinke R01423368

class SSNClass:
    def __init__(self):
        self.__ssn= "Still need to enter SSN in format ddd-dd-dddd"

    def setSSN(self, ssNumber):
        
        ssNumberDigits = ssNumber.replace("-" ,"")#So, i made it so they're allowed to input just 123456789 digits, or the formatted 123-45-6789 or anything with 9 numbers and only '-' ie ----123--4-56789
        if len(ssNumberDigits)==9 and ssNumberDigits.isdigit():# probably more user friendly, but can easily change with "and ssNumber[4]=='-' and ssNumber[7]=='-'"
             print("Valid SSN")
             formatted= ssNumberDigits[:3] + "-" + ssNumberDigits[3:5] + "-" +ssNumberDigits[5:]
                
             #print(ssNumberDigits,"and", ssNumber)
             self.__ssn= formatted #formatted the stored ssn
        else:
            print("Invalid SSN")

    def getSSN(self):
        return self.__ssn


        

def main():    
    ssnInput = input("Please enter your ssn in the format \"ddd-dd-dddd\": ") 
    ssNumber=SSNClass()
    ssNumber.setSSN(ssnInput)
    print(ssNumber.getSSN())
    

main()