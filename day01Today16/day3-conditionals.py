#!/usr/bin/python3

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#     print("Can ride")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#     elif age >=12 and age <= 18: # elif age <=18
#         bill = 7
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         bill = 12

#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == 'Y':
#         bill += 3

#     print(f"Your final bill is ${bill}")
# else:
#     print("Can't ride") 

# ---------------------------odd or even ----------------------------------------------
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("Your number is even (par)")
# else:
#     print("Your number is odd (inpar)")
# --------------------------- BMI 2.0----------------------------------------------
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = round(weight / height ** 2)
# print(f"Your BMI is {bmi}")
# if bmi < 18.5:
#     print("underweight ")
# elif bmi < 25:
#     print("normal weight")
# elif bmi < 30:
#     print("overweight")
# elif bmi < 35:
#     print("obese")
# else: print("clinically obese")
# --------------------------- Leap Year----------------------------------------------
# Flow chart : https://viewer.diagrams.net/?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Leap%20Algorithm#R7VpNc9owEP01HNuxJdmYY4CkzTTNdEpmmhyFrdhqhcXIIkB%2BfSUsY4wcQhqwC%2B0p0urDu29Xu08KHTiYLD4JPE2%2B8oiwDnCiRQcOOwC4CPjqj5Ysc0k3gLkgFjQyk0rBiD4TI3SMdEYjklUmSs6ZpNOqMORpSkJZkWEh%2BLw67ZGz6lenOCaWYBRiZkt/0EgmuTQA3VL%2BmdA4Kb7s%2Br18ZIKLycaSLMERn2%2BI4GUHDgTnMm9NFgPCNHgFLvm6qxdG14oJksp9FoDbYTJlQFxPomj0Jbzr4tT9YJTN5LIwmETKftPlQiY85ilml6W0L/gsjYje1VG9cs4N51MldJXwJ5FyaZyJZ5IrUSInzIwqhcXyXq//6BXdB7PdqjNcVHpL08t11Qq%2BCIERZXwmQrLD7iKUsIiJ3DEPrB2lIpzwCVH6qHWCMCzpU1UPbEItXs8rvaEaxiFvcI7Z9wmzmfnS6O7i%2B53lstIhGt15QiUZTfHK/rk6lVXwzZ5ESLLYDaNttlkAYE85brVoWZxWE%2BTz8oy4xRFONs4Hco6ElfePBjLYM5DhOwN5tfRCCLzcmDDlNJXZxs7ftKAMFLcLtgKlyOulq/M9S8evlfvzWPD/x8LOWHCdQwSD5W3kdre97W8d91w1s64Mg7fGFQLWl5qIK2Dl4%2BtMr9GahYzglGkjOsBnCv3%2BWKhWrFsRfaIZHas4A85YT0EdeGVn8YRPxrOsmQxe8Jcif3dr8jf07PwdHCt/QwvbW65xvSHK/HcVvEfK2IAzLlZr4WMQkjBU8kwK/otsjIwDD3nOYQB23SrA65PQWoHs1gBsAasMllX0MKNxqtqhMpwooPoaFqr48YUZmNAoyjMoyegzHq%2B20iiaQ6z29fodb6j3Ukkzy/PngeLYDSwm0rOBhjU4g2PhHFg4P5Ds5IGG/j5AoyaBdmErZX5B5X1RyFX7oaz4qlfWeN0pSvxfQA2KVPM6N2j3xhO06VP3XH2KWvWpcyjapG%2BZLRMn6IPX63pdvTkacXJtVnpwzhR5JIhQHWcKwBj6/oFIqVfFFtaR0kY5E2jnVeFESwzaMx2BVtMRaOd14ERLzL4%2BdXutlhh0qBKD2i8xyNum2rWJsI5rH6/I9M6lyHi9bXRRzUWm4TJjM6RzuDOi3hZXClq%2BMRYmnNcbCHS3I7oO6EbfQIDNSc8AaGQBDdt%2BbAL2s%2Bk5ZA47Sdch3WzusCnGST9QQ9RkHVTd8ocO%2Bb9jyp%2BLwMvf
# year = int(input("Which year do you want to check? "))

# # # first try
# # # if year % 4 == 0 and year % 100 != 0 and year % 400:
# # #     print("Leap")
# # # elif year % 4 == 0:
# # #     print("Leap")
# # # else:
# # #     print("Not Leap")

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap")
#         else:
#             print("Not Leap")
#     else:
#         print("Leap")
# else:
#     print("Not Leap")

# --------------------------- Pizza Order----------------------------------------------

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# small_pizza_price = 15
# medium_pizza_price = 20
# large_pizza_price = 25
# p_for_small = 2
# p_for_medium_large = 3
# extra_cheese_price = 1

# bill = 0

# if size == 'S':
#     bill += small_pizza_price
    

# elif size == 'M':
#     bill += medium_pizza_price
    
# else:
#     bill += large_pizza_price

# if add_pepperoni == 'Y':
#     if size == 'S':
#         bill += p_for_small
#     else:
#         bill += p_for_medium_large

# if extra_cheese == 'Y':
#     bill += extra_cheese_price


# print(f"Your final bill is ${bill} ")



# --------------------------- Love Calculator ----------------------------------------------

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")


# full_name = name1 + name2

# T = full_name.lower().count('t')
# R = full_name.lower().count('r')
# U = full_name.lower().count('u')
# E = full_name.lower().count('e')

# L = full_name.lower().count('l')
# O = full_name.lower().count('o')
# V = full_name.lower().count('v')
# E = full_name.lower().count('e')

# true_score = (T+R+U+E)
# love_score = (L+O+V+E)

# total_score = str(true_score) + str(love_score)
# int_total_score = int(total_score)
# print(total_score)
# if int_total_score < 10 or int_total_score > 90:
#     print(f"Your score is {total_score}, you go together like coke and mentos.")
# elif int_total_score >= 40 and int_total_score <= 50:
#     print(f"Your score is {total_score}, you are alright together.") 
# else:
#     print(f"Your score is {total_score}.")


# --------------------------- Project Treasure Island ----------------------------------------------

print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[______]
*******************************************************************************                                     


''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first_decision = input("Left or Right? ").lower()
if first_decision == 'left':
    second_decision = input("Swim or Wait? ").lower()
    if second_decision == 'wait':
        door_decision = input("Which door? Red/Blue/Yellow ").lower()
        if door_decision == 'red':
            print("Burned by fire.\n\nGAME OVER\n")
        elif door_decision == 'blue':
            print("Eaten by beasts.\n\nGAME OVER\n")
        elif door_decision == 'yellow':
            print("You found the treasure, You Win!")
        else:
            print("GAME OVER")

    else:
        print("Attacked by a trout.\n\nGAME OVER\n")
else:
    print("Fall into a hole.\n\nGAME OVER!\n")
