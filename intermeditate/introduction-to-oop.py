class Car():
  def __init__(self, brand, color):
    self.brand = brand
    self.color = color

  def honk(self):
    print("Beep beep!")


my_car = Car('Audi', 'orange')
print(my_car.brand)
print(my_car.color)

my_car.honk()