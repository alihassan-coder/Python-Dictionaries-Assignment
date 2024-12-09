# 14. Reverse the dictionary `{'a': 1, 'b': 2, 'c': 3}` so that keys become values and values become keys.

dictionary  = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = dict((values , key ) for key , values in dictionary.items())

print(reversed_dict)