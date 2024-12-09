# 28. Flatten the following nested dictionary into a single-level dictionary:  
#     ```python
#     {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}  
#     ```  

nested_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}

flattened_dict = {f"{outer_key}.{inner_key}": inner_value 
                  for outer_key, inner_dict in nested_dict.items() 
                  for inner_key, inner_value in inner_dict.items()}

print("Flattened dictionary:", flattened_dict)
