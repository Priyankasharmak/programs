#array 
def custome():
    a=[1,2,3,4,5]

    b=[0]* len(a)

    y=0

    for x in range(len(a)-1,-1,-1):

        b[y] = a[x]
        y+=1

    print(b)


# array functions
    
def arrayappend():

    a=[1,2,3,4,5]
    b=[]
    for x in range(len(a)-1,-1,-1):
        b.append(  a[x] ) 
    print(b)


def arraypop():
    a=[1,2,3,4,5 , 7]
    b = a.pop(1)
    print(b , "is removed by popping")
    print(a)


# arraypop()

def arrayrem():
    a=[1,2,3,4,5 , 7,8,9 ,4]
    a.remove(6)
    print(a)

# arrayrem()
 
def arryinster():
    a=[1,2,4,5,6,7]
    a.insert(0,8)
    print(a)


def arrrev():   
    a=[1,2,4,5,6,7]
    a.reverse()

    print(a)


def arrexte():   
    a=[1,2,4,5,6,7]
 
    a.extend([1,2,[1,2]])  
    print(a)
    

arrexte()
def arrind():   
    a=[1,2,4,5,6,7]
    a.index(6)
    print(a)



# arrind()