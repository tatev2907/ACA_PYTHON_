input_string = input("Enter a list elements separated by space: ")
userList = input_string.split()
print("user list is: ", userList)
s = input("Enter compearing element: ")
for i in userList:
    if s == i:
        userList.remove(i)
print("Output list is: ", userList)

'''
1. Տրված list-ից ջնջել տրված արժեքի բոլոր համընկնումները:
Իրականացնել հետևյալ մեթոդներով՝
ա. remove method
բ. list comprehension

'''
