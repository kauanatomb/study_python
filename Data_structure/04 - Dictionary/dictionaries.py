# declaring a dictionary
person = {
    "name": "Kauana",
    "age": 24,
    "city": "Brazil"
}

person2 = dict(name="Presti", age=23, city="France")

# Accessing datas
print(person["name"]) # Kauana
print(person.get("age")) # 24

# Adding datas
person["phone"] = "999-999-999"
print(person) # {'name': 'Kauana', 'age': 24, 'city': 'Brazil', 'phone': '999-999-999'}
person2["email"] = "presti@email.com"
print(person2) # {'name': 'Presti', 'age': 23, 'city': 'France', 'email': 'presti@email.com'}

# Removing datas
del person["phone"]
print(person) # {'name': 'Kauana', 'age': 24, 'city': 'Brazil'}
person2.pop("email")
# if the key does not exist, it will return an error
# person2.pop("email") # KeyError: 'email'
# to avoid this, you can use the second parameter
person2.pop("email", "Not found")
print(person2) # {'name': 'Presti', 'age': 23, 'city': 'France'}

# Changing datas
person["name"] = "Kauana Presti" 
person2["name"] = "Presti Kauana" 
print(person) # {'name': 'Kauana Presti', 'age': 24, 'city': 'Brazil'}
print(person2) # {'name': 'Presti Kauana', 'age': 23, 'city': 'France'}

# Nested dictionary
person3 = {
    "name": "Kauana",
    "age": 24,
    "address": {
        "street": "Street 1",
        "number": 123,
        "country": "Brazil"
    },
    "jobs": ["developer", "designer"],
    "email": {
        "email": "kauana@email.com"
    }
}

# Accessing nested dictionary
print(person3["email"]) # {'email': 'kauana@email.com'}
print(person3["jobs"][0]) # developer
print(person3["address"]["street"]) # Street 1

# Iterating through dictionary
for key, value in person3.items():
    print(key, value) 

# name Kauana, age 24, address {'street': 'Street 1', 'number': 123, 'country': 'Brazil'}, jobs ['developer', 'designer'], email {'email': 'kauana@email.com'}

# Combining dictionaries
info = dict(birthday="01/01/99")
person.update(info)
print(person) # {'name': 'Kauana Presti', 'age': 24, 'city': 'Brazil', 'birthday': '01/01/99'}
del person["birthday"]

# Or using **kwargs
info2 = dict(nacionality="Brazilian")
person4 = {**person, **info2}
print(person4) # {'name': 'Kauana Presti', 'age': 24, 'city': 'Brazil', 'nacionality': 'Brazilian'}

# Clearing dictionary
person.clear()
print(person) # {}

# Copying dictionary
person = person2.copy()
print(person) # {'name': 'Presti Kauana', 'age': 23, 'city': 'France'}

# Creating keys from a list
keys = ["name", "age", "city"]
person = dict.fromkeys(keys)
print(person) # {'name': None, 'age': None, 'city': None}

# Checking if key exists
print("name" in person) # True
print("phone" in person) # False
print("country" in person3["address"]) # True
person.get("name") # None
person.get("phone") # None

# Getting all keys
print(person.keys()) # dict_keys(['name', 'age', 'city'])

# Getting all values
print(person.values()) # dict_values([None, None, None])

# setting default value
person.setdefault("birthday", "01/01/99")
print(person) # {'name': None, 'age': None, 'city': None, 'birthday': '01/01/99'}
