import tkinter as tk

print("Welcome to the KPH to MPH converter")
print("-" * 5)

user_prompt = float(input("To begin, enter a speed in MPH that you would like to see in KPH: "))
conversion = round(user_prompt / 1.609, 2)

print("-" * 5)

print(f"MPH: {user_prompt} \nKPH: {conversion} ")
