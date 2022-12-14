#Kevin Brinke R01423368

filename = input('Enter a filename: ')
score_file = open(filename)

total_points = 0.0#total points for scores added up
count = 0#total scores
avg_score = 0

for line in score_file:
    #removes newline character
    line = line.strip()
    #splitting the line by space
    scores = line.split(' ')# an array of scores
    for i in scores:
        total_points += float(i)  
        count += 1 
if count>0:#undivisible by 0
    avg_score = total_points/count


print('There are',count,'scores')
print('The total is',total_points)
print('The average is {:.2f}'.format(avg_score))