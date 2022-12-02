isbn_9 = input("please enter the first 9 digits of an ISBN-10 as a string: ")
isbn_9 = isbn_9.strip()
list = list()
if isbn_9.isdigit():
    if len(isbn_9) == 9:
        print("is digit")
        for i in range(len(isbn_9)):
            list.append(isbn_9[i])
            print (list)
        for i in (list):
            d1,d2 = list[i:]
    print(d1,d2)
# d1,d2,d3,d4,d5,d6,d7,d8,d9 = int(list)
# print(d1,d2,d3,d4,d5,d6,d7,d8,d9)
# isbn_tenth_digit = eval(d1*1+ d2*2+ d3*3+ d4*4+ d5*5+ d6*6+ d7*7+ d8*8+ d9*9)

# print(isbn_tenth_digit)


# isbn_9.append(isbn_10_digit)





# d1,d2,d3,d4,d5,d6,d7,d8,d9 = isbn_9_stripped
# a1,a2,a3,a4,a5,a6,a7,a8,a9 = int(d1,d2,d3,d4,d5,d6,d7,d8,d9)
# print(a1,a2,a3,a4,a5,a6,a7,a8,a9)
# # isbn_9_add = int(d1+2*d2+3*d3+4*d4+5*d5+6*d6+7*d7+8*d8+8*d9)