def count_char(list1):
    count_b = 0
    d = []
    for c in list1[0]:
        if c not in d:
            # list of a counts same characters in strings
            n = list1[0].count(c)
            count_c = 1
            for j in range(1, len(list1)):
                if list1[j].count(c) >= 1:
                    count_c += 1
            if count_c == len(list1):
                count_b += 1
            d.append(c)
    return count_b


input_list = input("Input string list elements separated by space: ")
string_list = input_list.split()
print(count_char(string_list))
