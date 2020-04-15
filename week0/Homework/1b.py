input_string = input("Enter a list elements separated by space: ")
userList = input_string.split()
print("User list is ", userList)
s = input("Enter compearing element ")
userList = [i for i in userList if s != i]
print("Output list is ", userList)
