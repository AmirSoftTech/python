'''
i = 1
sum = 0
while i<=5:

    sum = sum + i
    i =i+1

    print(sum)
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
