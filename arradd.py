a=[1,3,2,4]
b=[4,5,2,1]
print("[",end="")   


for x in range(len(a)):
    c = a[x]+b[x]

    print(c ,end=",")
print("]")

