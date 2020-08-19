'''
#xargs example
def addFunction(*a):

    sum = 0
    for x in a:
        sum = sum + x
    print("Total sum : ", sum)

addFunction(10,10)
addFunction(10,10,10)
addFunction(10,10,10,10)

'''

'''
#xxargs example
def addFunction(**a):
        print(a)
addFunction(id=100, name="Amirul")

'''

def addFunction(*a):

    sum = 0
    for x in a:
        sum = sum + x
    return sum

x = addFunction(10,20)
print(x)
