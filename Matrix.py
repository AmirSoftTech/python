'''
matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for x in matrix:
   print(x)
'''

num1 = {1,2,3,4,5,6}
#num2 = set([5,6,7,8,9,10])

num2 = {5,6,7,8,9,10}

print(num1 | num2)

print(num1 & num2)

print(num1 - num2)