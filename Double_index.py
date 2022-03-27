# define a function that doubles the given index and returns it into the lst

def double_indexs(lst, index):
  print(lst[index])
  print(lst[index] * 2)
  lst[index] = lst[index] * 2
  return lst

print(double_indexs([3, 8, -10, 12], 2))
print("")

# Completed function

def double_index(lst, index):
  if index >= (len(lst)):
    return lst
  elif index <= (len(lst)):
    print(lst[index])
    print(lst[index] * 2)
    lst[index] = lst[index] * 2
    return lst
  else:
    return lst

print(double_index([3, 8, -10, 12], 2))