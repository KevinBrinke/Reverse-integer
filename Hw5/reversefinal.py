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
    return "-" + ans
  return ans

while(test):
  user_in = input("enter num: ")
  if user_in[0] == "-":
    flag = True
    user_in = user_in[1:]
  if not user_in.isdigit():
    print("not an integer")
  else:
    print(other_reverse(user_in))
    # print(reverse(int(user_in)))
    test = False