a=[7,3,5,1,2 ,4]

max=0
max2=0
for x in range(len(a)):
    if a[x] > max:
        max=a[x]

    if a[x] > max2 and a[x]<max:
        max2= a[x]
print(max)       
print(max2)
