# 9. Check if the key `grade` exists in the `student` dictionary and print `True` or `False`. 
student = {
    "name" : "Ali Hassan",
    "age" : "18",
    "grade" : "A+",
    "city" : "New York"
}

if student.get("grade") is not None:
    print("True")
else:
    print("False")
