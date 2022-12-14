from locationclass import Location


arr = Location()

row,col = 2,2#eval(input("Please enter the amount of rows and columns(seperated by comma) in the list: "))

for i in range(row):
    row_contents = input(f"Enter row {i} with {col} numbers: ")
    row_list = row_contents.split(" ")

    arr.create_arr(row_list,i,col)
    
# print(arr.get_arr())