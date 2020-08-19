n = int(input("Enter value : "))

i = 1
sum = 0
while i<=n:
    if i==6:
        break
    print(i)
    sum = sum + i
    i = i + 1
print("Sum of total number : ", sum)