'''
# n = 3
*
* *
* * *

#logic  2*i -1= 2*1 - 1 = 1
        2*i -1= 2*2 - 1 = 3
        2*i -1= 2*3 - 1 = 5
        2*i -1= 2*4 - 1 = 7

'''

'''
n = int(input("Enter the value : "))
for i in range(n+1):
    print(i*"*")


#Out put 
*
**
***

'''


'''
n = int(input("Enter the value : "))
for i in range(n+1):
    print((2*i-1)*"*")


#Output
*
***
*****

'''

rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
