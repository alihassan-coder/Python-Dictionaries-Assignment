# 13. Sort the keys of the dictionary `{'z': 1, 'a': 2, 'c': 3}` in ascending order and print the sorted dictionary.  

dictionary = {'z': 1, 'a': 2, 'c': 3}
sort_key = dict(sorted(dictionary.items()))

print(sort_key)