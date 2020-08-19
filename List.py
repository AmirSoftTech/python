'''
def my_Function(a, b, c):
    print("First name : ", a)
    print("Family name : ", b)
    print("Phone Number : ", c)

my_Function(

                input("First Name : "),
                input("Family Name : "),
                input("Phone Number : ")

            )
'''

'''

# Split list : 10,20,30 and sum
n = input("Enter the value : ")

list = n.split()

sum = 0

for num in list:
    sum = sum + int(num)
print("Sum of list : ", sum)
'''


word = 0
letter = 0
digit = 0

text = input("Enter Value : ")


for x in text:

    x = x.lower()

    if x>= 'a' and x<='z':
        letter = letter + 1

    elif x>='0' and x<'9':
        digit = digit+1

    elif x == ' ':
        word = word +1

print("Letter   : ",letter)
print("Word     : ",word)
print("Digit    : ",digit)






