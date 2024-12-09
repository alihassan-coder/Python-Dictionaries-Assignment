# 27. Write a Python program to create a dictionary where the keys are the first `n` positive integers, and the values are their cubes. Take `n` as user input. 

n = int(input("Enter the value of n: "))

cubes_dict = {i: i**3 for i in range(1, n+1)}

print("Dictionary of cubes:", cubes_dict)




