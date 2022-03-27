# Create a function that removes the first middle three elements of the lst

def remove_middle(lst, start, end):
  lst.pop(1)
  lst.pop(1)
  lst.pop(1)
  return lst

#Code academies approach
#def remove_middle(lst, start, end):
  #return lst[:start] + lst[end+1:]

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
print("")

# Retrying the function using code academies method

def remove_the_middle(lst, start, end):
  lst2 = sorted(lst)
  print(lst2)
  return lst2[:start] + lst2[end + 1:]


print(remove_the_middle([4, 8, 6, 3, 51, 62, 13, 22, 15, 16, 23, 42], 3, 6))
