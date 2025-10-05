import os

# Get the folder where *this script* lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build a full path to index.html
html_path = os.path.join(BASE_DIR, "Big O.txt")

counter = 0

# Reading line by line
with open(html_path, 'r', encoding="utf8") as file:
    for line in file:
        counter += 1
        #print(line.strip()) # .strip() removes leading/trailing whitespace, including newline

print(f"Number of lines in txt file: {counter}")