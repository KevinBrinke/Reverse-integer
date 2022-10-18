#Kevin Brinke R01423368


def reverse(user_in):
    revNum = user_in[::-1]
    if flag :
        revNum = "-" + revNum
        eval(revNum)
    return revNum



test = True
flag = False

while(test):
  userIn = input("enter num: ")
  if userIn[0] == "-":
    flag = True
    if not userIn.isdigit():    
        print("not an integer")
    else:
        test = False


revInt=reverse(userIn)
print(revInt)