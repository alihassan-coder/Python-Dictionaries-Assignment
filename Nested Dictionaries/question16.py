# 16. Create a nested dictionary to represent the following data:  
    # ```plaintext
    # Person:  
    #   Name: John  
    #   Age: 30  
    #   Address:  
    #     Street: 123 Elm St  
    #     City: Boston  
    # ```  
Person = {
      "Name" : "John",
      "Age" : "30",
      "Address" : {
          "street" : "123 Elm St",
          "City" : "Boston",
      }
}
print(Person)