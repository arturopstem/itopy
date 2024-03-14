prices = [250, 300, "240", 400]
try:
  total = sum(prices)
  print(total)
except TypeError:
  print("Invalid data type")

print("Happy Shopping")

color = "Green"
try:
  print(size)
except NameError:
  print("Check the variable name")

colors = ["Red", "Yellow", "Green"]
try:
  print(colors[10])
except IndexError:
  print("Out of range")
except NameError:
  print("Variable is not defined")

price = input("Enter price: ")
try:
  price_value = int(price)
except ValueError:
  print("Please enter a number")