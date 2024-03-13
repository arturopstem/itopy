words = ["tree", "button", "cat", "window", "defenestrate"]

# Use a list comprehension to filter out words longer than four letters
long_words = [x for x in words if len(x) > 4]

# Display the filtered list
print(long_words)