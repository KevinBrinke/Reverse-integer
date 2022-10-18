number =25
isprime=True
i=2
while i<number and isprime:
    if number %i ==0:
        isprime=False
    i+=1
print("i is",i,"isprime is", isprime)