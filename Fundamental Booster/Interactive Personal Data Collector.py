# Welcome Statement
print("Welcome to the Interactive Personal Data Collector!")
print() 

# Taking input from user
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
number = int(input("Please enter your favourite number: "))
print()

# Generating a thankyou message
print("Thank you! Here is the information we collected:")
print()

# Type() and id() Functions
print(f"Name: {name} (Type: {type(name)}, Memory Address:{id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address:{id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address:{id(height)})")
print(f"Favourite Number: {number} (Type: {type(number)}, Memory Address:{id(number)})")
print()

# Birth Year Approximation
from datetime import datetime
# current year
Current_Year = datetime.now().year

# Calculating the birth year
Birth_Year = Current_Year - age

# based on age the estimated birth year
print(f"Your birth year is approximately: {Birth_Year} (based on your age of {age})")
print()
# Last the thankyou message
print("Thank you for using the Personal Data Collector. Goodbye!")