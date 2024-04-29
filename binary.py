a=[0,1,2,3,4,5,6,7,8,9,10]
# c=5
c=int(input("enter the element:"))
l=0
r=len(a)-1
while l<=r:
    
    b=(l+r)//2
    if a[b]==c:
        print("got at",b)
        break
    elif a[b]<c:
        l=b+1
    else:
        r=b-1

if l>r:
    print("not got")