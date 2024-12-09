# 15. Write a Python function to check if two dictionaries are identical (contain the same key-value pairs). 

def chack_identical(dic1 , dic2):
    if dic1 == dic2:
        print("This is Identical")
    else:
        print("This is not Identical")

dic1 = {
    "a" : "1",
    "b" : "2"
}
dic2 = {
    "a" : "1",
    "b" : "2"
}
chack_identical(dic1 , dic2)