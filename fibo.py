a=0
b=1
print(a , end=' ')
print(b, end=' ')
for x in range (0,5):
    c=a+b
    print(c, end=' ')
    a=b
    b=c

