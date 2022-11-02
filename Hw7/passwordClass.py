#Kevin Brinke R01423368



class PasswordCheck:
    def __init__(self):
        self.__password= "no password created"
        
    def setPassword(self):
        passCheck= 1
        while passCheck is False:
            self.__password=input("Enter a password word with the following conditions:\n\t1.Must be at least 8 characters\n\t2.Must consist of only digits and letters\n\t3.Must contain at least 2 digits\n\nNew Password: ")
            if len(self.__password) < 7:
                passCheck = 0
                return
            










def main():
    account= PasswordCheck()
    account.setPassword()


main()