input_string = input("Enter a list elements separated by space: ")
userList = input_string.split()
def dup_del(w):
    w=set(w)
    return w
print(dup_del(userList))