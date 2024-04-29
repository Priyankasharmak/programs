a = [ [1,2] , [2,3,5,6] , [3,4] ]
b = [ [2,3] , [4,5,5,6] , [5,6] ]
c = a

# twod=[]
# for x in range(len(a)):
#     oned=[]
#     for y in range(len(a[x])):
#         oned.append(a[x][y]+b[x][y])
#     twod.append(oned) 
# print(twod)
# print(a)

for x in range(len(a)):
    for y in range(len(a[x])):
        c[x][y]=a[x][y]+b[x][y]

print(c)
print(a)
