# 23. Create a dictionary to map numbers 1 to 5 to their squares (e.g., `{1: 1, 2: 4, 3: 9, ...}`).

def square(num):
    result = num * num
    return result

num = [1 ,2 , 3, 4, 5]

dec = { num : square(num) for num in num}
print(dec)