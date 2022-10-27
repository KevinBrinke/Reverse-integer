#Kevin Brinke r01423368
#account test

from account import Account

def main():
    a1= Account()

    a1.setID(1122)
    a1.setBalance(20000)
    a1.setAIR(4.5)
    a1.withdraw(2500)
    a1.deposit(3000)

    print(a1.getID(),":personal Id")

    print("$",a1.getBalance(),":current balance")

    print(a1.getMIR(),"% per month")

    print("$",a1.getMI(),":Monthly interest")





main()