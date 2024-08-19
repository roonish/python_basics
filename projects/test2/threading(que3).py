import threading

# Lock object to synchronize threads
lock = threading.Lock()

# Function to print even numbers
def print_even():
    # Start from 2, go up to 10, step by 2
    for i in range(2, 11, 2):  
        # Acquire the lock before printing
        with lock:  
            print(f"Even: {i}")

# Function to print odd numbers
def print_odd():
    # Start from 1, go up to 9, step by 2
    for i in range(1, 10, 2): 
         # Acquire the lock before printing 
        with lock: 
            print(f"Odd: {i}")

# Create threads for even and odd number printing
even_thread = threading.Thread(target=print_even)
odd_thread = threading.Thread(target=print_odd)

# Start the threads
even_thread.start()
odd_thread.start()

# Wait for both threads to finish
even_thread.join()
odd_thread.join()

print("Done!")
