'''
#Example for Tuple
tuple1 = ("green", "red", "blue") #Create tuple
print(tuple1)

tuple2 = tuple([7, 1, 2, 34, 6, 8]) #Create a tuple from a list
print(tuple2)

print("length is ", len(tuple2)) #Use len function
print("Max is ", max(tuple2)) #use max
print("Min is ", min(tuple2)) #use min
print("Sum is ", sum(tuple2)) #use sum

print("The first element is ", tuple[0]) #Use index operator

tuple3 = tuple1 + tuple2 #Combine two tuples
print(tuple3)

tuple3 = 2 * tuple1 #Duplicate a tuple
print(tuple3)

print(tuple2[2 : 4]) #Slicing operations
print(tuple1[-1])

print(2 in tuple2) # in operator

for v in tuple1:
    print(v, end = ' ')
print()

list1 = list(tuple2) #obtain a list from a tuple
list1.sort()
tuple4 = tuple(list1)
tuple5 = tuple(list1)
print(tuple4)
print(tuple4 == tuple5) #Compare two tuples

'''









'''
# Demo the sets
set1 = {"green", "red", "blue", "red"} #Create a set
print(set1)

set2 = set([7, 1, 5, 8, 23, 44, 46, 6]) #Create a set from a list
print(set2)

print("Is red in set1?", "red" in set1)

print("length is ", len(set2)) #Use len function
print("Max is ", max(set2)) #use max
print("Min is ", min(set2)) #use min
print("Sum is ", sum(set2)) #use sum

set3 = set1 | {"green" , "yellow"} # Set union
print(set3)
print(set1)
set3 = set1 - {"green" , "yellow"} # Set difference
print(set3)

set3 = set1 & {"green" , "yellow"} # Set intersection
print(set3)

set3 = set1 ^ {"green" , "yellow"} # Set excusive or
print(set3)

list1 = list(set2) #obtain a list from a set
print(set1 == {"green", "red", "blue"}) #Compare two sets

set1.add("yellow")
print(set1)

set1.remove("yellow")
print(set1)
'''









# '''
# Demo for Dictionaries
students = {}
students["234-56-9010"] = "Susan" #Adding an item to dictionary in the format key:value
students = {"111-34-3434":"John", "132-56-6290":"Peter"} #Adding multiple items
students["234-56-9010"] = "Susan" #Adding an item to dictionary in the format key:value

print(students["111-34-3434"]) #Seaching a value by its key
# students["111-11-1111"] #Demo for key error when key doesn't exist in the dict container
# del students["234-56-9010"] #Del the key and value from dict.
for key in students:
    print(key + ":" + str(students[key])) # To display all the elements read from the dict via a loop
len(students) # Returns number of items in a dictionary
"111-34-3434" in students #to check if key exist in dict. Returns bool output
students2 = {"red":41, "blue":3}
students3 = {"blue":3, "red":41}
print(students2 == students3)
students2 != students3
print(tuple(students.keys())) #Return a sequence of keys
print(tuple(students.values())) #Return a sequence of values
print(tuple(students.items())) #Return a sequence of tuples. Each tuple is (key:value) for an item
print(students.get("111-34-3434")) #Returns the value for the keys
print(students.pop("111-34-3434")) #Removes the item for the key and return its value
print(students.get("111-34-3434")) #Returns the value for the keys
print(students)
students.clear() #Deletes all entries
# '''



