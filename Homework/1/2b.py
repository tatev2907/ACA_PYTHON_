input_string = input("Enter a list elements separated by space: ")
userList = input_string.split()
[userList.remove(i) for i in userList if userList.count(i)> 1 for j in range(userList.count(i)-1)]
print(userList)