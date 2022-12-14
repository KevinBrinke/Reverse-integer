r,c=str(input("Enter rows and columns: ")).split(',')
r=int(r)
c=int(c)
list1=[]
maxi=[]
idx=[]
for i in range(0,r):
    a=list(map(float,input("Enter row {}:".format(i)).rstrip().split()))
    list1.append(a)
    maxi.append(max(a))
    idx.append(a.index(max(a)))
maxi_row=maxi.index(max(maxi))
maxi_col=idx[maxi_row]
print("The location of largest element is {} at row[{},{}]".format(max(maxi),maxi_row,maxi_col))