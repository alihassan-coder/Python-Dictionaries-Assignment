# 8. Iterate through the dictionary `student` and print all key-value pairs in the format `key: value`.

student = {
    "name" : "Ali Hassan",
    "age" : "18",
    "grade" : "A+",
    "city" : "New York"
}
for keys , values in student.items():
    print(keys  + " : " + values)