def fact(n):
    if n == 1:
        return 1
    else:
        return n *fact(n-1)


a = int(input("Enter the value for factorial : "))

x = fact(a)

print("Result of factorial : ",x)