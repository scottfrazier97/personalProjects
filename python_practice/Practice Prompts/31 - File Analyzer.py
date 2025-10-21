#File Line Analyzer: 
# Read a file
# Count how many lines contain digits
# Count how many lines are empty
# Return the longest line (by char count)

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
txt_file = os.path.join(BASE_DIR, "Big O.txt")

digit_lines_counter = 0
empty_lines_counter = 0
longest_line = ""

with open(txt_file, 'r', encoding="utf8") as file:
    for line in file:
        stripped = line.strip()

        if not stripped:
            empty_lines_counter += 1
        elif any(ch.isdigit() for ch in stripped):
            digit_lines_counter += 1

        if len(stripped) > len(longest_line):
            longest_line = stripped

print(f"Number of empty lines: {empty_lines_counter}\nNumber of digit lines: {digit_lines_counter}\nLongest line: {longest_line}")