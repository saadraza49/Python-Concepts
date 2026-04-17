# Dictionary
dict1 = {
    "name" : "Saad", 
    "age" : 21,
    "gender" : "male"
    }
dict1["city"] = "Faisalabad"
dict1.pop("age") # remove age
print(dict1.keys()) # print keys (NAME, AGE, GENDER)
print(dict1.values()) # print values (SAAD, MALE, FAISALABAD)
print(dict1.items()) # print items (EVERTHING)
dict1.update({"country" : "Pakistan"}) # add country
# OR
dict1["country"] = "Pakistan"
dict1.popitem() # remove last item
print(dict1)