guests = {"Mery", "Anna", "Jonathan"}
print(guests)

friends = {"Anna", "Mery", "Mery", "Jonathan"}
print(friends)

guests.add('Robert')
guests.remove('Mery')
print(guests)

set1 = {"apple", "banana"}
set2 = {"banana", "cherry"}
combined_set = set1.union(set2)
print(combined_set)

set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "orange"}
unique = set1.difference(set2)
print(unique)