# 30. Create a dictionary comprehension to filter out all keys in `{'a': 1, 'b': 2, 'c': 3, 'd': 4}` where the value is less than 3.

original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

filtered_dict = {key: value for key, value in original_dict.items() if value >= 3}

print("Filtered dictionary:", filtered_dict)
