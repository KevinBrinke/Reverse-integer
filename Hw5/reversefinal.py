#Kevin Brinke R01423368
#Q2


test = True
flag = False
#using math
# def reverse(num):
#   revNum = 0
#   while num != 0:
#     d = num % 10
#     revNum = revNum * 10 + d
#     num //= 10
#   if flag:
#     return revNum * -1
#   return revNum

def other_reverse(num):#using string
  revAns = num[::-1]
  if flag:
    revAns=eval("-" + revAns)
   # return "-" + revAns
  return revAns

while(test):
  userIn = input("Enter number that will be reversed: ")
  if userIn[0] == "-": #global flag to add negative back to integer later, so .isdigit works
    flag = True
    userIn = userIn[1:]#eliminates 0th position of string which will be negative 
  if not userIn.isdigit():
    print("not an integer")
  else:
    print("The reversed number is: ",other_reverse(userIn))
    # print(reverse(int(userIn)))
    test = False