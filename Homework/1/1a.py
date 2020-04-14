input_string = input("Enter a list elements separated by space: ")
userList = input_string.split()
print("user list is: ", userList)
s = input("Enter compearing element: ")
n=len(userList)
i=0
for c in range(n):
    if s == userList[i]:
        userList.remove(userList[i])
    else:
        i+=1
print("Output list is: ", userList)
