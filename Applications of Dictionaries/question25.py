# 25. Write a Python function that accepts a dictionary and a key, and returns the value associated with the key. If the key doesn’t exist, return `"Key not found"`.


dictionary = {'a': 10, 'b': 15, 'c': 10, 'd': 15}

def func( dictionary , key):
    return dictionary.get(key ,"key not found" )

print(func(dictionary , "u"))