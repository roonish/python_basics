import math

# Base class Shape
class Shape:
    def area(self):
        # Base method returns 0, as it doesn't know the shape's specifics
        return 0

    def __str__(self):
        # Base string representation of the shape
        return "This is a generic shape."

# Derived class Rectangle inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        # Initialize the width and height attributes
        self.width = width
        self.height = height

    def area(self):
        # Calculate and return the area of the rectangle
        return self.width * self.height

    def __str__(self):
        # String representation of the rectangle
        return f"Rectangle with width {self.width} and height {self.height}"

# Derived class Circle inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        # Initialize the radius attribute
        self.radius = radius

    def area(self):
        # Calculate and return the area of the circle
        return math.pi * self.radius ** 2

    def __str__(self):
        # String representation of the circle
        return f"Circle with radius {self.radius}"
    
# ............................................................
# Demonstrating the use of inheritance and calculating areas

# Create an instance of Rectangle
rect = Rectangle(4, 5)
 # Print the string representation of the rectangle
print(rect)    
 # Calculate and print the area of the rectangle          
print(f"Area: {rect.area()}") 

# Create an instance of Circle
circ = Circle(3)
# Print the string representation of the circle
print(circ)    
 # Calculate and print the area of the circle           
print(f"Area: {circ.area()}") 
