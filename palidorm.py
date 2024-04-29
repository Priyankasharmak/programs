a="Eye".upper()
b=""
for x in range(len(a)-1,-1,-1):
    b+=a[x]
        
print(b)    

if a==b:
    print("palidorm:")
else:
    print("not palidorm:")    