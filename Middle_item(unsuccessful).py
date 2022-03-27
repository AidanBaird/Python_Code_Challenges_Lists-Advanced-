def middle_element(lst):
    if len(lst) % 2 == 0:
        i = len(lst) / 2
        print(i)
        return (int(lst[i] + lst[i + 1])) / 2
    elif len(lst) % 2 == 1:
        i = len(lst) / 2
        # print(i)
        index = round(i)
        # print(index)
        # print("")
        return lst[index]


print(middle_element([5, 2, -10, -4, 4, 5]))