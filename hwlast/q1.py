class Location:
    def __init__(self,row=0,column=0,maxValue=0):
        self.row = row
        self.column = column
        self.max_value = maxValue

    def __str__(self):
        return "(Row : " + str(self.row) + " Column : " + str(self.column) + " Value : " + str(self.max_value) + ")";


def max_location(list):
    row_loc=0
    col_loc=0
    
    for i in range(len(list)):
        for j in range(len(list[0])):
    #update maximum
            if list[i][j]>list[row_loc][col_loc]:
                row_loc = i
                col_loc = j
    return Location(row_loc,col_loc,list[row_loc][col_loc])

print('Enter the number of rows and columns in the list: ', end='');
data = input().strip().split(',')
rows = int(data[0].strip())
cols = int(data[1].strip())

ans = list()
for i in range(rows):
    print('Enter row ' + str(i) + ': ', end='')
    data = input().strip().split()
    l = []
    for x in data:
        l.append(float(x))
    ans.append(l)

loc = max_location(ans)
print('The location of the largest element '+str(loc.max_value)+' is at ('+str(loc.row)+', '+str(loc.column)+')')