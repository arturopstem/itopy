prices = [559, 879, "N/A", 349]
try:
  print(sum(prices))
except TypeError:
  print("Check the prices")
finally:
  print("Need help? Contact us")

books = ["Harry Potter", "Dune", "Emma"]
try:
  choice = books[1]
except IndexError:
  print("Out of range")
else:
  print(choice + " is a great choice!")

# print("Rate from 0 to 10")
# rate = 15
# if rate > 10 or rate < 0:
#   raise ValueError

rating = 15
if rating > 10  or rating < 0:
  raise ValueError("Rate from 0 to 10")

