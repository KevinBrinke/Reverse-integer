# ZIP
def add_items(l1, l2):
    result = [] # define an empty list to hold the result
 
    # aggregate each item of the lists
    # for each iteration, item1 and item2 comes from l1 and l2 respectively
    for item1, item2 in zip(l1, l2):
        result.append(item1 + item2) # add and append.
 
    return result
 
if __name__ == '__main__':
    list_1 = [4,6,1,9]
    list_2 = [9,0,2,7]
 
    print("RESULT: ", add_items(list_1, list_2))
l1 = [3,4,7] # list with size 3
l2 = [0,1]   # list with size 2(shortest iterable)
l3 = list(zip(l1,l2))
print(l3)
# [(3, 0), (4, 1)]


#MAP(), ZIP(list1,list2)
#map changes all elements by the functions described (ie x+2)
lst = [4,5,2,6,7]
lst2 = list(map(lambda x: x+2,lst))
print(lst)
print(lst2)

l1 = [6,4,8,9,2,3,6]  # list of size 7
l2 = [0,1,5,7,3]      # list of size 5(shortest iterable)
l_zip_map = list(map(lambda x,y: (x+2,y+2), l1,l2)) #lambda accepts two args
#[(8, 2), (6, 3), (10, 7), (11, 9), (4, 5)]
print(l_zip_map)


#FILTER()
names = ["john","petter","job","paul","mat"]
name_filtered =list(filter(lambda name: len(name) <= 4, names))
print(name_filtered)
# ['john', 'petter', 'paul']
names = ["1234124","1234","123","5555","0000"]
name_filtered =list(filter(lambda name: len(name) == 4, names))
# ['john', 'petter', 'paul']
print(name_filtered)
names = ["1234124","1234","123","5555","0000"]
name_filtered =list(filter(None,[False,0,{},6,50,'30']))
# [ignores the none or false flags]
print(name_filtered)


#ALL()
#true if all elements are true or empty
#l= [[]] is a list of an empty list and will produce false
l = [0, 6, "today"]
print(all(l))
#true

#ANY()
# if any are true will give true
#empty list will give false unlike all()
l1 = ['hi',[4,9],-4,True,False] # not all is true
print(any(l1))
# True
l2 = ['',[],{},False,0,None] # all is false
print(any(l2))
# False