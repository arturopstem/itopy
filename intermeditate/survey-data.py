user_answers = ["Yes", "", "No", "", "Maybe", "", "Yes"]

# Create a new list without empty answers
# using filter with a lambda expression
cleaned_list = list(filter(lambda ans: len(ans) > 0, user_answers))

# Display the cleaned list of answers
print(cleaned_list)