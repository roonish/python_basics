class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of the Person class
person1 = Person("Ronish Siwakoti", 24)

# Call the greet method
person1.greet()
