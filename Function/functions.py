# Declaring a simple function
def greet():
    print("Hello, World!")

# Declaring a function with parameters
def greet_person(name, age):
    print(f"Hello, {name}, you are {age} years old!")

# Declaring a function with default parameters
def greet_person_default(name="Kauana", age=24):
    print(f"Hello, {name}, you are {age} years old!")

# Kwargs identifier allows you to pass a dictionary as a parameter
def greet_person_kwargs(name, age):
    print(f"Hello, {name}, you are {age} years old!")

# Example of using the functions
greet() # Hello, World!
greet_person("Kauana", 24) # Hello, Kauana, you are 24 years old!
greet_person_default() # Hello, Kauana, you are 24 years old!
greet_person_default("Presti", 23) # Hello, Presti, you are 23 years old!
greet_person_kwargs(**{"name":"Kauana", "age":24}) # Hello, Kauana, you are 24 years old!

# Positional only parameters 
# The / symbol indicates that the parameters before it are positional only
def greet_person_positional(name, age, /, city):
    print(f"Hello, {name}, you are {age} years old and live in {city}!")

print(greet_person_positional("Kauana", 24, "Brazil")) # Hello, Kauana, you are 24 years old and live in Brazil!
print(greet_person_positional("Kauana", 24, city="Brazil")) # Hello, Kauana, you are 24 years old and live in Brazil!
# Error examples
# print(greet_person_positional(name="Kauana", age=24, "Brazil")) # SyntaxError: positional argument follows keyword argument
# print(greet_person_positional(name="Kauana", age=24, city="Brazil")) # TypeError: greet_person_positional() got some positional-only arguments passed as keyword arguments: 'name, age'

# Keyword only parameters
# The * symbol indicates that the parameters after it are keyword only
def greet_person_keyword(name, age, *, street):
    print(f"Hello, {name}, you are {age} years old and live in the {street}!")

print(greet_person_keyword("Kauana", 24, street="Street 5")) # Hello, Kauana, you are 24 years old and live in the Street 5!
# Error examples
# print(greet_person_keyword("Kauana", 24, "Street 5")) # TypeError: greet_person_keyword() takes 2 positional arguments but 3 were given
# print(greet_person_keyword("Kauana", 24, "Street 5", street="Street 5")) # TypeError: greet_person_keyword() got multiple values for argument 'street'

# Keyword and positional parameters
def greet_person_all(name, age, /, city, *, country):
    print(f"Hello, {name}, you are {age} years old and live in {city}, {country}!")

print(greet_person_all("Kauana", 24, city="SP", country="Brazil")) # Hello, Kauana, you are 24 years old and live in SP, Brazil!
print(greet_person_all("Kauana", 24, "SP", country="Brazil")) # Hello, Kauana, you are 24 years old and live in SP, Brazil!
# Error examples
# print(greet_person_all("Kauana", 24, "Brazil", "Brazil")) # TypeError: greet_person_all() takes 3 positional arguments but 4 were given
# print(greet_person_all(name="Kauana", age=24, city="Brazil", country="Brazil")) # TypeError: greet_person_all() got an unexpected keyword argument 'name'

# Global and local variables
city = "France"

def greet_person_global(name, age):
    global city
    print(f"Hello, {name}, you are {age} years old and live in {city}!")

# Lambda functions
def add(a, b):
    return a + b

add_lambda = lambda a, b: a * b
print(add_lambda(2, 5)) # 10
print(add(1, 2)) # 3

# Map function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared) # [1, 4, 9, 16, 25]

# Filter function
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even) # [2, 4]




