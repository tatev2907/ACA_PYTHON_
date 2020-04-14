input_string = input("Enter a list elements separated by space: ")
userList = input_string.split()
userList.sort()
n = len(userList)
t=False
print(userList)
if n != 0:
    for i in range(1, n):
        if (int(userList[0] )!= 1):
            print(1)
            t = True
            break
        elif int(userList[i]) - int(userList[i - 1]) != 1:
            print(int(userList[i]) - 1)
            t=True
            break
    if i == n or not t:
        print(int(userList[n - 1]) + 1)

else:
    print(1)
