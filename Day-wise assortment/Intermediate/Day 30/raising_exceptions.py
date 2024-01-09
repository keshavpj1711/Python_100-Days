# This is an example for where can we actually use raising our own exceptions

# Writing a program to calculate BMI
height = float(input("Enter your height in meters: "))
weight = float(input("Enter you weight in kgs: "))

# Raising an exception if height over 3m is input
if height > 3:
    raise ValueError("Humans can not have heights over 3 meters")
if weight > 500:
    raise ValueError("Humans can not weigh more than 500kgs")

# Calculating the BMI
bmi = weight/(height ** 2)
print(f"Your BMI: {round(bmi, 2)}")