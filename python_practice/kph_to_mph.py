import tkinter as tk

print("Welcome to the KPH to MPH converter!")
print("- " * 5)

user_speed_prompt = float(input("To begin, enter a speed in MPH: "))
conversion = round(user_speed_prompt / 1.609, 2)
print("-" * 5)

print(f"MPH: {user_speed_prompt} \nKPH: {conversion} ")


