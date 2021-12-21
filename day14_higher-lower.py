# Breakdown

# Compare followers in the elements of the list of dictionaries in game data
# Get randomly 2 elements of the dictionary and show to the user
# Ask the user if A or B has more followers
# If the user is correct increment the score +1, otherwise end the game
# Show the game logo, the current score, compare A, VS logo, Against B
# The format of the compairing string must be: Compare A: name, Description, Country


from day14_art_logo import logo, vs
from day14_game_data import data
import random
import itertools
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# [{'name': 'Instagram', 'follower_count': 346, 'description': 'Social media platform', 'country': 'United States'}, 

def format_data(account):
    """Takes the account data and returns printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        # if guess == "a":
        #     return True
        # else:
        #     return False
        return guess == "a"
    else:
        return guess == "b"

# Display art 
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    
    # Generate a random account from the game data

    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")


    # Ask user for a guess

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    ## Get tfollower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    ## Use if statement to check if the user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    ## Score keeping.
    # Clear the screen
    cls()
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right!, your score is {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score {score} ")



    

print(“What would you like? (espresso/latte/cappuccino):")
    









# ----------- Structure lab
#print(type(data))
# print(data[1]['follower_count'])
# print(data[1])
# print(data[2])

#print(len(data))
# for val in range(len(data)):
#     print(data[val]['follower_count'])




#RCSolution ----------------------------------------------------------
# def getCompare():
#     i = random.randint(0,len(data))
#     print(f"Compare A: {data[i]['name']}, {data[i]['description']},from {data[i]['country']}")
#     return i

# def getAgainst():
#     i = random.randint(0,len(data))
#     print(f"Against B: {data[i]['name']}, {data[i]['description']},from {data[i]['country']}")
#     return i

# getCompare()
# print(vs)
# getAgainst()

# question = input("Who has more followers? Type 'A' or 'B': ")
# score = 0
# compareA = data[getCompare()]['follower_count']
# compareB = data[getAgainst()]['follower_count']

# #print(data[getCompare()]['follower_count'])

# keep_playing = False
# while keep_playing:
#     if question == 'A' and compareA > compareB:
#         print("You're right! ")
#         score +=1
#         print(score)
#     elif question == 'B' and compareB > compareA:
#         print("")
#         score +=1
#         print(f"You're right!, score: {score}")
#     elif question == 'A' and compareA < compareB:
#         print(f"Sorry, that's wrong. FInal score: {score}")
#         keep_playing = False
#     elif question == 'B' and compareB < compareA:
#         print(f"Sorry, that's wrong. FInal score: {score}")
#         keep_playing = False
#     else:
#         print("Provide a valid option. ")

