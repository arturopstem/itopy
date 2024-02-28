def rect(length, width):
  area = length * width
  perimeter = 2 * length + 2 * width
  return area, perimeter

x, y = rect(50, 100)
print(x, y)

def greet(name = "Guest"):
  print("Welcome", name)

greet()
greet("John")