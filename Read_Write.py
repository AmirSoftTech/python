#File read
'''
file = open("student.txt","r+")
y = file.readlines()[1]
print(y)
file.close()

'''

'''
#File read using for loop
file = open("student.txt","r+")
for line in file:
    print(line)
file.close()
'''

'''
#File write 'a'= means add new line with existing content  
file = open("student.txt","a")
file.write("\nI am a  novice programmer!!")

file.close()

#File write 'w' = means overwrite with existing content 
file = open("student.txt","w")
file.write("\nI am a  novice programmer!!")

file.close()

'''