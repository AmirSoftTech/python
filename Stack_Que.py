'''
# Example of stack
stack = []

stack.append("C")
stack.append("C++")
stack.append("Java")
stack.append("Python")

print(" Total number of book on the stack : ", stack)

stack.pop()
print(" After pop now the total number of book left on the stack : ", stack)
print(" and the position of the top book is : ", stack[-1])

'''


#Example of
from collections import deque

bank = deque(["Rahim", "Karim", "Asad", "Shahin"])

print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()
if not bank:
    print("No person left")
