a = [1,2,3,4,5,6,7,8]
b = [2,3,4,5]

c=[]

for x in range(len(b)):
    c.append(a[x]+b[x])

for y in range(len(b) , len(a)):
    c.append(a[y])

print(c)   
