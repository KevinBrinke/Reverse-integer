#kevin Brinke R01423368
from smallestElement import indexOfSmallestElement


lst = []
run = True
while run:
    ui = input("Enter a list of integers, hit enter between each, type \"e\" to stop: ")
    if ui.isdigit():
        lst.append(ui)
    else:
        run = False
    print(lst)
if len(lst)> 1:
    print(indexOfSmallestElement(lst))
else:
    print("invalid list")