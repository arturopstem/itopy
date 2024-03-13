user = {
  "Name": "Albert",
  "Age": 29
}
user.update({"Age":30})
print(user)

user.update({"Age":30, "Surname":"Johnson"})
print(user)

car = {
  "Brand": "Ford",
  "Model": "Mustang",
  "Color": "red"
}

for i in car:
  print(i)

for i in car.values():
  print(i)

print(car)
print("Color" in car)
print("red" in car.values())
car.pop("Color")
print(car)
print("Color" in car)
print("red" in car.values())