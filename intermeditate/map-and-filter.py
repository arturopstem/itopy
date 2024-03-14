# Map
names = ["alice", "bob", "CHARLIE", "Tom"]
def capitalize(name):
  return name.capitalize()

capitalized = map(capitalize, names)
print(capitalized)

capitalized = list(capitalized)
print(capitalized)


prices = [25.99, 14.50, 8.75, 19.95]
def discount(price):
  discount_price = price * 0.9
  return discount_price

discounted_price = list(map(discount, prices))
print(discounted_price)

exam_scores = [85, 62, 95, 40, 78]
def is_passing(score):
  return score >= 70

status = list(map(is_passing, exam_scores))
print(status)

numbers = [1, 2, 3]
doubled = list(map(lambda x: x * 2, numbers))

print(doubled)

# Filter
products = ["Table", "Sofa", "Cushion", "Bookshelf", "Vase"]

filtered_prod = list(filter(lambda name: len(name) == 4, products))
print(filtered_prod)

products = {
  'Table': 110,
  'Sofa': 120,
  'Chair': 45,
  'Lamp': 70
}
filtered = dict(filter(lambda item: item[1] < 90, products.items()))
print(filtered)