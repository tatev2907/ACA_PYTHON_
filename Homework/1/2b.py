input_string = input("Enter a list elements separated by space: ")
userList = input_string.split()
newL = []
newL = [i for i in userList if i not in newL]
print(newL)