print("Welcome to the tip calculator.\n")
total = input("What was the total bill? \n")
tip_percentage = input("What percentage tip woud you like to give? 10, 12 or 15? \n")
split_bill = input("How many people to split the bill: ")
total_account = float(total) + float(total) * (float(tip_percentage) / 100)
pay_per_person = total_account / float(split_bill)

print(f"Each person should pay: ${round(pay_per_person,2)}")