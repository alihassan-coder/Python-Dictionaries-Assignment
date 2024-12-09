# 24. Write a Python program to remove duplicate values from the dictionary `{'a': 10, 'b': 15, 'c': 10, 'd': 15}`.

dec = {'a': 10, 'b': 15, 'c': 10, 'd': 15}
uniqe_dec = {}
seen = set()

for key ,value in dec.items():
    if value not in seen:
        uniqe_dec[key] = value
        seen.add(value)

print(uniqe_dec)