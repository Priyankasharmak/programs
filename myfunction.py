
def function(a):
    b=[]
    for x in range(len(a)):
        if a[x] not in b:
            b.append(a[x])

    return b 




t = [1,2,3,4,5,6,2,3,4]


r = function(t)
print(r)
