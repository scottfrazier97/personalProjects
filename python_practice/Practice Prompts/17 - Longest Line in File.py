import os

# Get the folder where *this script* lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build a full path to index.html
html_path = os.path.join(BASE_DIR, "Big O.txt")

longest_line = ""
counter = 0

# Reading line by line
with open(html_path, 'r', encoding="utf8") as file:
    for line in file:

        counter += 1

        if len(line) > len(longest_line):
            longest_line = line.strip()
            longest_line_number = counter
        else:
            continue

print(f"Line number: {longest_line_number}\nLongest line in txt file:{longest_line}")