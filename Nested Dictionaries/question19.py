# 19. Delete the `Address` key from the nested dictionary. 
Person = {
      "Name" : "John",
      "Age" : "30",
      "Address" : {
          "street" : "123 Elm St",
          "City" : "Boston",
      }
}
del Person["Address"]
print(Person)