# 17. Access the value of the `City` key in the nested dictionary from the previous question. 
Person = {
      "Name" : "John",
      "Age" : "30",
      "Address" : {
          "street" : "123 Elm St",
          "City" : "Boston",
      }
}
print(Person["Address"]["City"])