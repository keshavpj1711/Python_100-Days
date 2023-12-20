# Greetings
print("Welcome to Tip Generator")

# Getting total cost
total_bill = float(input("What was the total bill? Rs"))

# Asking about the percentage of tip
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))

# Splitting the bill
total_people = int(input("How many people to split the bill? "))

# Per person cost
per_person_cost = (total_bill*(1 + tip_percentage/100))/total_people
print(f"Each person should pay: Rs{round(per_person_cost, 2)}")