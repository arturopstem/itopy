def greet():
  print("Hello from a function")
  print("Have a great day")

greet()

def personal_greet(name):
  print("Hello", name)
  print("Have a great day")

personal_greet("Arturo")

def bmi(weight, height):
  index = weight / (height * height)
  return index

print(bmi(75, 1.74))