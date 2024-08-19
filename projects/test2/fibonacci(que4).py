def fibonacci_generator():
    # Initial two Fibonacci numbers
    a, b = 0, 1
    
    while True:
        yield a  # Yield the current value of 'a'
        a, b = b, a + b  # Update 'a' and 'b' to the next two Fibonacci numbers

# Create the Fibonacci generator
fib_gen = fibonacci_generator()

# Print the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))
