import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while guess != number_to_guess:
        guess = int(input("Take a guess: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

guess_the_number()
