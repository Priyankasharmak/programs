

a=input("enter the string:")
b=['a' , 'e' , 'i' , 'o' , 'u']
count=0
for x in range(len(a)):
    for y in range(len(b)):
        if a[x]==b[y]:
            count+= 1



# for x in a:
#     if x in b:
#         count+=1

print("total  vowels are ",count)    
