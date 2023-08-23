# capitals = {"Jalisco": "guadalajara", "Nuevo Leon": "Monterrey"}
# # Add a new entry to the dictionary
# capitals["Chiapas"] = "Tuxtla Gutierrez"
# # Edit an item in a dictionary
# capitals["Jalisco"] = "Guadalajara"
# # Empty a dictionary
# #capitals = {}
# # Loop through a dcitionary
# for key in capitals:
#     print(key + "-" + capitals[key])
#     #print(capitals[key])
#--------------------------------------Day-9-1- Students Score Exercise----------------------------------------
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     if student_scores[student] > 90:
#         student_grades[student] = "Outstanding"

#     elif student_scores[student] > 80:
#         student_grades[student] = "Exceeds Expectations"

#     elif student_scores[student] > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
    
# # 🚨 Don't change the code below 👇
# print(student_grades)

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇

# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)



# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

from day9_logo import logo
import os


print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner =""
    # bidding_record = {"Ricardo" : 34, "Axel":45}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount # highest_bid BECOMES the bid_amount
            winner = bidder
    print(f"The winner is the {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What's your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls')
        

   

# WRONG LOGIC REGARDING LOOPING DICTIONARIES
    # # # else:
        
    # # #     max_value = 0
    # # #     for key, value in bid_db.items():
    # # #         winner = ''
    # # #         if int(value) > max_value:
    # # #             winner = key
    # # #             max_value = value
    # # #         print(f"The winner of the bid is {winner} with a bid of {max_value}")
        














def add_new_bid(name, bid):
    bid_db = {}
    
    bid_db[name] = bid_price

    bid_log = [
        {
            "name" : "Ricardo",
            "bid" : 23
        }
    ]
    bid_log.append(bid_db)

active_bid = True
