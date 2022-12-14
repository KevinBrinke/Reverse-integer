#Kevin Brinke R01423368

class Location:
    def __init__(self, row=0, column=0, max_value=0):
        self.max_value = max_value
        self.row = row
        self.column = column

def locate_largest(list_2d):
    largest = Location(0, 0, list_2d[0][0])
    for i in range(len(list_2d)):
        for j in range(len(list_2d[i])):
            if list_2d[i][j] > largest.max_value:
                largest = Location(i, j, list_2d[i][j])
    return largest


def main():
    matrix = []
    num_rows = int(input("Enter the number of (only) rows in the list: "))
    for i in range(num_rows):#need input of rows, 
        matrix.append([float(column.strip()) for column in input("Enter row {}: ".format(i)).split()])
    largest = locate_largest(matrix)
    print("The location of the largest element is {} at ({}, {})".format(largest.max_value, largest.row, largest.column))


main()