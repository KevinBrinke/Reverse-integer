#Kevin Brinke R01423368

isbn_9 = input("Enter the first 9-digit of an ISBN as a string: ")
list = [isbn_9]

if len(isbn_9) != 9 or isbn_9.isdigit() is False:
    print("Incorrect input")
else:

    #Calculate checksum
    sum = (ord(isbn_9[0]) - ord('0')) + (ord(isbn_9[1]) - ord('0'))*2 + (ord(isbn_9[2]) - ord('0'))*3 \
    + (ord(isbn_9[3]) - ord('0'))*4 + (ord(isbn_9[4]) - ord('0'))*5 + (ord(isbn_9[5]) - ord('0'))*6 \
    + (ord(isbn_9[6]) - ord('0'))*7 + (ord(isbn_9[7]) - ord('0'))*8 + (ord(isbn_9[8]) - ord('0'))*9
    check_sum = sum % 11
    
    if check_sum == 10:
        check_sum= "X"
    else:
        check_sum = str(check_sum)
    list.append(check_sum)
    isbn_10 = list[0]+ list [1] 
    print("The ISBN number is", isbn_10)
    

    