# a=[3,1,2,5,4,7,9]
a=[9,8,6,5,4,3,2,1]
for y in range(len(a)):
     for x in range(len(a)-1):
         if a[x]>a[x+1]:
             b=a[x+1]
             a[x+1]=a[x]
             a[x]=b
print(a)  
