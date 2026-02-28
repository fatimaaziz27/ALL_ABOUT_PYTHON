# Q) What will be the output of the following code?

students = [
    {"name":"sara","age": 18},
    {"name":"yusra","age":14}
]
print(students[1]["name"])

# OUTPUT:
# yusra

# Q) What will be the output of the following code?

products = [
    {"item":"laptop","price":800},
    {"item":"phone","price":500}
]
products[0]["price"]=750
print(products)

# OUTPUT:
# [{'item': 'laptop', 'price': 750}, {'item': 'phone', 'price': 500}]

# Q) What will be the output of the following code?

books = [
    {"title":"harry potter","author":"j.k. rowling"},
    {"title":"1984","author":"george orwell"}
]
books.append({"title":"the hobbit","author":"j.r.r. tolkien"})
print(books)

# OUTPUT:
# [{'title': 'harry potter', 'author': 'j.k. rowling'}, {'title': '1984', 'author': 'george orwell'}, {'title': 'the hobbit', 'author': 'j.r.r. tolkien'}]

# Q) What will be the output of the following code?

classes = {
    "math":["alice","bob"],
    "science":["charlie","david"]
}
print(classes["science"])

# OUTPUT:
# ['charlie', 'david']

# Q) What will be the output of the following code?

classes = {
    "math":["alice","bob"],
    "science":["charlie","david"]
}
classes["math"].append("emma")
print(classes)

# OUTPUT:
# {'math': ['alice', 'bob', 'emma'], 'science': ['charlie', 'david']}