#Kevin Brinke R01423368

#getting file name
filename=input('Enter a filename: ')
#opening file
score_file=open(filename) #will raise exception if file not found
#defining variables to store total and count
total=0.0
count=0
#looping through all lines in file (will work even if there are multiple lines)
for line in score_file:
#removing trailing newline character
    line=line.strip()
#splitting the line by whitespace to generate an array of values
    numberText=line.split(' ')
#going through the array
    for i in numberText:
#converting each array element into float and adding to total
        total+=float(i)
#incrementing count
        count+=1
#finding average
avg=0
if count>0:
#dividing by count only if count>0, to prevent division by 0
    avg=total/count
#displaying all stats
print('There are ',count,'scores')
print('The total is',total)
#printing average with 2 decimal points precision
print('The average is {:.2f}'.format(avg))