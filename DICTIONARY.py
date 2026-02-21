# Q) What will be the output of the following code? 

data = {
    "city":"new york",
    "country":"USA"
}
data["population"] = 8_000_000
print(data)

# OUTPUT:
# {'city': 'new york', 'country': 'USA', 'population': 8000000}

# Q) What will be the output of the following code? 

person = {
    "name":"alice",
    "age":25
}
print(person["age"])

# OUTPUT:
# 25

# Q) What will be the output of the following code? 

person = {
    "name":"bob",
    "age":50
}
person["age"] = 28
print(person)

# OUTPUT:
# {'name': 'bob', 'age': 28}


# Q) What will be the output of the following code? 

info = {
    "brand":"ford",
    "year":2020
}
del info["year"]
print(info)

# OUTPUT:
# {'brand': 'ford'}

# Q) What will be the output of the following code? 

car = {
    "brand":"toyota",
    "model":"camry"
}
print("model" in car)

# OUTPUT:
# True
