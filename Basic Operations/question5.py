# 5. Remove the key `city` from the `student` dictionary.  

student = {
    "name" : "Ali Hassan",
    "age" : "18",
    "grade" : "A+",
    "city" : "New York"
}

# using del mathod
del student["city"]
print(student)

#using pop()
a = student.pop("city")
print(student)