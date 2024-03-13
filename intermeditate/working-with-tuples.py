scores = (7, 9, 9, 8, 9)
print(scores.count(7))
print(scores.count(9))
print(scores.count(2))

points = (12, 14, 9, 10, 9)
print(points.count(9))
print("length:",len(points))
print("max:", max(points))

for point in points:
  if point > 10:
    print(point, ": passed")

# tuple unpacking
birthday_date = (12, "August", 1993)
day, month, year = birthday_date
print("day:",day)
print("month:", month)
print("year:", year)

scores = (98, 96, 91, 88, 64)
winner, *rest = scores
print(winner)
print(rest)