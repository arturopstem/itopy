# This throws exception:
# TypeError: total() takes 3 positional arguments but 4 were given
# def total(x, y, z):
#   return x + y + z
# print(total(2, 1, 3, 3))

def total(numbers):
  result = 0
  # iterating over the list
  for i in numbers:
    result += i
  return result

nums = [x for x in range(1, 6)]
print(total(nums))


# * is the unpacking operator
def total(*args):
  result = 0
  for arg in args:
    result += arg
  return result

print(total(1, 2, 3, 4, 5))
print(total(1, 2, 3, 4, 5, 6, 7))
print(total(1, 2, 3))

def show_items(category, *items):
  print("Category: "+ category)
  for item in items:
    print(item)

show_items("Electronics", "Laptop", "Smartphone", "Tablet")

#**kwargs is a dictionary
# ** operator unpacks dictionaries into arguments
def display_info(**kwargs):
  #kwargs.items() returns the key:valie pairs
  for key, value in kwargs.items():
    print(key, ":", value)

display_info(name="Alice", age=30, city="New York")