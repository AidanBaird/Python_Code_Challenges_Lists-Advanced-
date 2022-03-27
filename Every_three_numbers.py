# Create a function that adds three to start until it is at or above 100

def every_three_nums(start):
  return list(range(start, 101, 3))

print(every_three_nums(91))
print("")
print(every_three_nums(73))
print("")
print(every_three_nums(101))