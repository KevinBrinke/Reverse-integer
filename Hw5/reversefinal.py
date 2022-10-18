test = True
flag = False

# def reverse(num):
#   rev_num = 0
#   while num != 0:
#     d = num % 10
#     rev_num = rev_num * 10 + d
#     num //= 10
#   if flag:
#     return rev_num * -1
#   return rev_num

def other_reverse(num):
  ans = num[::-1]
  if flag:
    ans=eval("-" + ans)
   # return "-" + ans
  return ans

while(test):
  userIn = input("enter num: ")
  if userIn[0] == "-":
    flag = True
    userIn = userIn[1:]
  if not userIn.isdigit():
    print("not an integer")
  else:
    print(other_reverse(userIn))
    # print(reverse(int(userIn)))
    test = False