'''
#Lamda function
a =((lambda a : a*a*a)(4))
print(a)
'''

'''
#Filter function
num = [1,2,3,4,5,]

x  = list(filter(lambda a : a % 2 ==0, num))

print(x)
'''

'''
#map function
def square(x):
    return x*x
l  = [1,2,3,4,5,6]
x = list(map(square, l))
print(x)

'''

num = [1,2,3,4,5,]

x  = list(map(lambda a : a*a, num))

print(x)