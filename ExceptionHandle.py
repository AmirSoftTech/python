'''
#Exception Handle
try:
    a = [20, 0, 30]

    c = a[0] / a[1]

    print("Result : ", c)
    print("Done")
except ZeroDivisionError:
    print("Not possible")

finally:
    print("Index Error")
'''

a = 10
b = 20

print("a = ", a,",b = ",b)
a,b = b,a

print("a = ", a,",b = ",b)




