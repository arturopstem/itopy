def song_name(name):
  return "Song name: " + name

def info(name, func):
  print(func(name))

info("Hallelujah", song_name)

def outer_function():
  print("Hello from the outer function")

  def inner_function():
    print("Hello from the inner function")

  inner_function()

outer_function()

def greet(name):
  print("Hey", name)
  def account():
    return "Your account is created!"
  message = account()
  return message

print(greet("Bob"))

# Decorators example
# def greet():
#   return "Welcome!"

def uppercase(func):
  def wrapper():
    orig_message = func()
    modified_message = orig_message.upper()
    return modified_message
  return wrapper

# greet_upper = uppercase(greet)
# print(greet_upper())

# @ sign decorator
@uppercase
def greet():
  return "Welcome!"

print(greet())

# same decorator to several different functions
def stock_status_decorator(func):
    def wrapper(item):
        result = func(item)
        print(result, ": stock status for", item)
        return result
    return wrapper

@stock_status_decorator
def restock_item(item):
    return "Restocked"

@stock_status_decorator
def sell_item(item):
    return "Sold"

print(restock_item("Laptop"))
print(sell_item("Smartphone"))