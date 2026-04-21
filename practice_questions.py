# Best practice questions:

"""
Basic inheritance?

Q) Create a class 'Animal' with a method 'speak()' that prints "Animal speaks".
Now create a subclass 'Dog' that inherits from 'Animal' and overrides the 'speak()' method to print "Dog barks".
Create objects of both classes and call the 'speak()' method.

"""
# ANSWER:

class Animal:
    def speak(self):
        """Prints a generic animal sound"""
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        """Overrides the speak method to print a dog's sound"""
        print("Dog barks")
animal = Animal()
dog = Dog()
animal.speak()  
dog.speak()

# OUTPUT:

# Animal speaks
# Dog barks

"""
Multi-Level Inheritance

Q) Create a class 'Vehicle', then create a subclass 'Car', and then a subclass 'ElectricCar' that inherits from 'Car'.
Each class should have one method that prints something specific to that class.
Create an object of 'ElectricCar' and call all methods from each level.

"""
# ANSWER:

class Vehicle:
    def vehicle_method(self):
        """Prints a message specific to Vehicle"""
        print("This is a vehicle.")
class Car(Vehicle):
    def car_method(self):
        """Prints a message specific to Car"""
        print("This is a car.")
class ElectricCar(Car):
    def electric_car_method(self):
        """Prints a message specific to ElectricCar"""
        print("This is an electric car.")
electric_car = ElectricCar()
electric_car.vehicle_method()      
electric_car.car_method()       
electric_car.electric_car_method() 

# OUTPUT:

# This is a vehicle.
# This is a car.
# This is an electric car.

"""
Polymorphism with Functions


Q) Create two classes: 'Circle' and 'Square'.
Both should have a method called 'area()' that calculates and returns their respective areas.
Write a function 'print_area(shape)' that accepts an object and calls its 'area()' method.
Pass objects of both classes to this function and print the result.

"""
# ANSWER:

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle"""
        return 3.14159 * (self.radius ** 2)

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        """Calculates and returns the area of the square"""
        return self.side ** 2

def print_area(shape):
    print(f"The area of the shape is: {shape.area()}")

circle = Circle(5)
square = Square(4)

print_area(circle)
print_area(square)

# OUTPUT:

# The area of the shape is: 78.53975
# The area of the shape is: 16

# Q) Rotate string left (`abc` → `bca`)

# ANSWER:

s = "abc"
print(s[1:] + s[0])

# OUTPUT:
# bca

# Q) Reverse words in sentence without slicing. 

# ANSWER:

sentence = "Hello World"
words = sentence.split()
reversed_words = [word[::-1] for word in words]
print(' '.join(reversed_words))

# OUTPUT:

# olleH dlroW


