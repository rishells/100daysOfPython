import random
from day12_art import logo

random_number = random.randint(1,100)

print(logo)
print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100")
print(f"Pssst, the correct answer is {random_number}")
difficulty = input("Choose a difficulty. Type 'easy or 'hard': ")
attempts = 0
if difficulty == 'easy'.lower():
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("Choose a valid option.")

while attempts > 0:
    print(f"You have {attempts} remaining to guess the number")
    user_guess = int(input("Make a guess: "))
    if user_guess < random_number:
        print("Too Low")
    elif user_guess > random_number:
        print("Too high")
    elif user_guess == random_number:
        print("You win, you guessed the number :) ")
        break
    elif attempts == 0:
        print("You've run out of attempts. You lose")
    else:
        print("Provide a valid parameter")
    attempts -= 1
    
    

