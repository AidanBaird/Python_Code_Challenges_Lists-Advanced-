# Create a function that counts and compares the frequency of item1 and item2 showing up in lst and returns the more
# commonly found item

def more_frequent_item(lst, item1, item2):
    a = lst.count(item1)
    print(a)
    b = lst.count(item2)
    print(b)
    if lst.count(item1) > lst.count(item2):
        return item1
    if lst.count(item1) == lst.count(item2):
        return "There are the same amount of items"
    else:
        return item2


print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
print("")
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 2))
print("")
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 3, 2))