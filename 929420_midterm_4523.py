# # Q1. Create two threads as follows:
# # Thread A counts odd numbers between 0 and 100
#  stepping five, i.e. 1, 3, 5, …, 99. 
# Thread B counts even numbers 0, 2, 4, 6, …, 100. 
# Run your threads and display the output on console.
#  In order to distinguish between the treads, use the following format:
# # Thread A: 1
# # Thread B: 0
# # Thread A: 3
# # …
# # …

import threading

def count_odds():
    """Thread A: Count odd numbers between 0 and 100, stepping by 2."""
    for i in range(1, 100, 2):
        print(f"Thread A: {i}")

def count_evens():
    """Thread B: Count even numbers between 0 and 100, stepping by 2."""
    for i in range(0, 101, 2):
        print(f"Thread B: {i}")

# Create the threads
thread_a = threading.Thread(target=count_odds)
thread_b = threading.Thread(target=count_evens)

# Start the threads
thread_a.start()
thread_b.start()

# Wait for both threads to complete
thread_a.join()
thread_b.join()

print("Counting completed.")

# ..................................................................

# Q2. You are requested to develop a 
# function (getNextPrime) in python that
#  returns prime numbers in sequence whenever 
# it’s called. For instance, the first call to
#  this function will return 3, the next call will
#  return 5, the next 7, the next 11, and 13 and so on.

class PrimeGenerator:
    def __init__(self):
        # Start from the first prime number
        self.current = 2  
    
    def is_prime(self, n):
        """Helper function to check if a number is prime."""
        if n <= 1:
            # Numbers less than or equal to 1 are not prime
            return False  
        if n <= 3:
            # 2 and 3 are prime numbers
            return True  
        if n % 2 == 0 or n % 3 == 0:
            # Eliminate multiples of 2 and 3
            return False  
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                # Check divisibility by i and i+2
                return False  
            # Increment by 6 to check next possible prime factors
            i += 6  
             # If no factors found, n is prime
        return True 
    
    def getNextPrime(self):
        """Return the next prime number in sequence."""
        while True:
            if self.is_prime(self.current):
                next_prime = self.current
                self.current += 1
                return next_prime
            self.current += 1

# Instantiate the prime generator
prime_gen = PrimeGenerator()

# Function to get the required number of prime numbers
def generate_primes(n):
    primes = []
    for _ in range(n):
        # Get the next prime number
        primes.append(prime_gen.getNextPrime())  
    return primes

# Ask the user for the number of prime numbers they want
num_primes = int(input("Enter the number of prime numbers you want: "))

# Generate and print the prime numbers
prime_numbers = generate_primes(num_primes)
print(prime_numbers)

# .......................................................................

#Q3. Define a class called BookStore to maintain the record of books sold.
#  The store contains three categories of books i.e. “Kids”, “Engineering”, 
# and “Story”. The following details should be maintained for each book.
# a. Book category
# b. Author
# c. Title
# d. Publisher
# e. Selling price of the book
# f. Quantity
# Create a constructor that initializes the Store ID and the rest of the 
# details of the book mentioned above. Include a method named 
# trackSalesStatus that will display the total number of books sold
#  by the store (add a static variable that tracks the total number 
# of books sold). Also, include a method to display the quantity 
# available corresponding to each Book ID. Write a main method to
#  test your class.

class BookStore:
    # Static variable to track the total number of books sold
    total_books_sold = 0  

    def __init__(self, store_id, category, author, title, publisher, selling_price, quantity):
        # Initialize book details
        self.store_id = store_id
        self.category = category
        self.author = author
        self.title = title
        self.publisher = publisher
        self.selling_price = selling_price
        self.quantity = quantity

    def sell_book(self, quantity_sold):
        # Sell a specified quantity of the book if available
        if quantity_sold > self.quantity:
            print(f"Not enough stock to sell {quantity_sold} books. Only {self.quantity} available.")
            return False
        self.quantity -= quantity_sold
        BookStore.total_books_sold += quantity_sold
        print(f"{quantity_sold} book(s) sold.")
        return True

    def track_sales_status(self):
        # Display the total number of books sold across all instances
        print(f"Total number of books sold: {BookStore.total_books_sold}")

    def display_quantity(self):
        # Display the current quantity available for this book
        print(f"Store ID: {self.store_id}, Title: {self.title}, Quantity Available: {self.quantity}")

def main():
    # Create book instances
    book1 = BookStore(store_id=1, category="Kids", author="Author A", title="Kids Book 1", 
                      publisher="Publisher A", selling_price=100, quantity=50)
    book2 = BookStore(store_id=2, category="Engineering", author="Author B", title="Engineering Book 1", 
                      publisher="Publisher B", selling_price=200, quantity=30)
    book3 = BookStore(store_id=3, category="Story", author="Author C", title="Story Book 1", 
                      publisher="Publisher C", selling_price=150, quantity=20)

    # Sell books
    sell_books(book1, 5)
    sell_books(book2, 10)
    sell_books(book3, 2)

    # Track sales status
    track_sales_status(book1)

    # Display quantity available
    display_quantities(book1, book2, book3)

def sell_books(book, quantity):
    # Sell a specified quantity of books and handle the process
    success = book.sell_book(quantity)
    if not success:
        print(f"Failed to sell {quantity} books for '{book.title}'.")

def track_sales_status(*books):
    # Track and display the total number of books sold
    if books:
        books[0].track_sales_status()

def display_quantities(*books):
    # Display the quantity available for each book
    for book in books:
        book.display_quantity()

if __name__ == "__main__":
    main()

# .....................................................................................

# Q4. Define a class called Fraction. This class is used to represent a ratio of two integers. 
# Include mutator methods that allow the user to set the numerator and the denominator. 
# Also include a method that displays the fraction on the screen as a ratio (e.g., 5>9). 
# This method does not need to reduce the fraction to lowest terms. Include an additional method, 
# equals, that takes as input another Fraction and returns true if the two fractions are identical
#  and false if they are not. This method should treat the fractions reduced to lowest terms; that is,
#  if one fraction is 20>60 and the other is 1>3, then the method should return true.
# Embed your class in a test program that allows the user to create a fraction. 
# Then the program should loop repeatedly until the user decides to quit.
#  Inside the body of the loop, the program should allow the user to enter a target fraction
#  into an anonymous object and learn whether the fractions are identical.

import math

class Fraction:
    def __init__(self, numerator=0, denominator=1):
        # Ensure the denominator is not zero during initialization
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator

    def set_numerator(self, numerator):
        self.numerator = numerator

    def set_denominator(self, denominator):
        # Ensure the denominator is not zero when setting a new denominator
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.denominator = denominator

    def display(self):
        # Display the fraction in the format numerator>denominator
        print(f"{self.numerator}>{self.denominator}")

    def equals(self, other_fraction):
        # Reduce both fractions to their lowest terms
        gcd_self = math.gcd(self.numerator, self.denominator)
        gcd_other = math.gcd(other_fraction.numerator, other_fraction.denominator)

        reduced_self_numerator = self.numerator // gcd_self
        reduced_self_denominator = self.denominator // gcd_self

        reduced_other_numerator = other_fraction.numerator // gcd_other
        reduced_other_denominator = other_fraction.denominator // gcd_other

        # Compare the reduced forms of the fractions
        return (reduced_self_numerator == reduced_other_numerator and
                reduced_self_denominator == reduced_other_denominator)

def create_fraction():
    # Loop until a valid fraction is created
    while True:
        try:
            num = int(input("Enter the numerator for the fraction: "))
            denom = int(input("Enter the denominator for the fraction: "))
            return Fraction(num, denom)
        except ValueError as e:
            # Handle invalid input and zero denominator
            print(e)
            print("Please enter valid integers and ensure the denominator is not zero.")

def main():
    print("Create the initial fraction.")
    # Create the initial fraction
    fraction1 = create_fraction()
    
    while True:
        # Display the current fraction
        print("Current Fraction: ", end="")
        fraction1.display()

        # Prompt the user to enter a target fraction
        num = input("Enter the numerator for the target fraction (or type 'quit' to exit): ")
        if num.lower() == 'quit':
            break
        
        try:
            # Parse the numerator and denominator for the target fraction
            num = int(num)
            denom = int(input("Enter the denominator for the target fraction: "))
            target_fraction = Fraction(num, denom)

            # Check if the fractions are identical
            if fraction1.equals(target_fraction):
                print("The fractions are identical.")
            else:
                print("The fractions are not identical.")
        except ValueError as e:
            # Handle invalid input and zero denominator for the target fraction
            print(e)
            print("Please enter valid integers and ensure the denominator is not zero.")
    
    print("Program terminated.")

if __name__ == "__main__":
    main()
