'''
# 1 + 2 + 3 + .... + n
n = int(input("Enter the value : "))
sum = 0
for x in range(1, n+1, 1):

    sum = sum + x

print("Sum of series  : ", sum)

'''


'''
# 2 + 4 + 6 + .... + n
n = int(input("Enter the value : "))
sum = 0
for x in range(2, n+1, 2):

    sum = sum + x

print("Sum of series  : ", sum)
'''


'''
# 1 + 3 + 5 + .... + n
n = int(input("Enter the value : "))
sum = 0
for x in range(1, n+1, 2):

    sum = sum + x

print("Sum of series  : ", sum)

'''


'''
# 1^2 + 2^2 + 3^2 + .... + n^2
n = int(input("Enter the value : "))
sum = 0
for x in range(1, n+1, 1):

    sum = sum + 1/x # Logic here in this case

print("Sum of series  : ", sum)
'''

'''
# 1 * 2 *3 * ... *n
n = int(input("Enter the value : "))
sum = 1
for x in range(1, n+1, 1):

    sum = sum * x

print("Sum of series  : ", sum)
'''

'''
# 2 * 4 * 6 * ... *n
n = int(input("Enter the value : "))
sum = 1
for x in range(2, n+1, 2):

    sum = sum * x

print("Sum of series  : ", sum)
'''

'''
# 3 * 5 * 7 * ... *n
n = int(input("Enter the value : "))
sum = 1
for x in range(3, n+1, 2):

    sum = sum * x

print("Sum of series  : ", sum)
'''

'''
# 1^2 * 2^2 * 3^2 * .... * n^2
n = int(input("Enter the value : "))
sum = 1
for x in range(1, n+1, 1):

    sum = sum * x*x

print("Sum of series  : ", sum)

'''

# 2^2 * 4^2 * 6^2 * .... * n^2
n = int(input("Enter the value : "))
sum = 1
for x in range(2, n+1, 2):

    sum = sum * x*x

print("Sum of series  : ", sum)

