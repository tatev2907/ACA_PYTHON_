input_string = input("Enter a list elements separated by space: ")
userList = input_string.split()
newL = []
for i in userList:
    if i not in newL:
        newL.append(i)
print("New List", newL)
