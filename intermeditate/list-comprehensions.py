# nums = []
# for x in range(1, 51):
#   nums.append(x)
# print(nums)

# list comprehensions
nums = [x for x in range(1,51)]
print(nums)

nums = [x*2 for x in range(10)]
print(nums)

num = [x+1 for x in range(10)]
print(num)

tags = ["travel", "vacation", "journey"]
hashtags = ["#" + x for x in tags]
print(hashtags)

cities = ['madrid', 'paris', 'lisabon']
cities_cap = [x.capitalize() for x in cities]
print(cities_cap)

sports = ["Football", "Basketball", "Tennis", "Golf", "Volleyball"]
group = [x for x in sports if "ball" in x]
print(group)