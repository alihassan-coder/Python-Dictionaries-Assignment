# 29. Write a Python program to split a dictionary into two based on whether the values are odd or even.  

original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

odd_dict = {key: value for key, value in original_dict.items() if value % 2 != 0}
even_dict = {key: value for key, value in original_dict.items() if value % 2 == 0}

print("Dictionary with odd values:", odd_dict)
print("Dictionary with even values:", even_dict)
