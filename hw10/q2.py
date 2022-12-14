#Kevin Brinke R01423368


def findGrades(lst):
    new_list = [int(x) for x in lst ]
    best = (max(new_list))
    i = 0

    while i < len(lst):
        scr = int(lst[i])

        if scr >= best - 10:

            print("Student ", i, " score is ", scr, " and grade is A")
        elif scr >= best - 20:
            print("Student ", i, " score is ", scr, " and grade is B")
        elif scr >= best - 30:
            print("Student ", i, " score is ", scr, " and grade is C")
        elif scr >= best - 40:
            print("Student ", i, " score is ", scr, " and grade is D")
        else:
            print("Student ", i, " score is ", scr, " and grade is F")
        i += 1


def main():

    scores = (input("Enter scores: "))
    lst = (scores.split())
    findGrades(lst)


main()