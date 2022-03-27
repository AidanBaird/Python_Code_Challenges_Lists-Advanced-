def middle_element(lst):
    if len(lst) % 2 == 0:
        sum = lst[int(len(lst) / 2)] + lst[int(len(lst) / 2) - 1]
        return sum / 2
        return sum / 2
    else:
        i = len(lst) / 2
        # print(i)
        index = round(i)
        # print(index)
        # print("")
        return lst[index]


print(middle_element([5, 2, -10, -4, 4, 5]))

# print(middle_element([1, 5, 2, -10, -4, 4, 5]))