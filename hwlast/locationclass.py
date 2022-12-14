


class Location:
    def __init__(self):
        self.row = 0
        self.column = 0
        self.max_value = 0
        self.arr =  []

    def create_arr(self, row_contents,row,col):
        lst_row = []

        for i in range(len(row_contents)):
            print(row_contents[i])
            lst_row.extend(row_contents[i])

        self.arr.append(lst_row)
        print(self.arr)
    
    def get_arr(self):
        return self.arr
    def set_row(self,row):
        self.row = row
    
    
    def set_column(self,column):
        self.column = column
    

    def get_row(self):
        return self.row
    def get_column(self):
        return self.column


    def set_max_value(self,max_value):
        self.max_value = max_value

    def get_max_value(self):
        return self.max_value

   


