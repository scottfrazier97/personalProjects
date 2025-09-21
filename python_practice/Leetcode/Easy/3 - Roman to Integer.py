# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

rn = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def roman_numeral_conversion():

    user_input = input("Input a roman numeral: ").strip().upper()

    total = 0
    i = 0

    while i < len(user_input):
        
        current_value = rn[user_input[i]]
        
        # Look ahead to the next character (if there is one)
        if (i + 1) < len(user_input):
            next_value = rn[user_input[i + 1]]

            # If the next value is larger, subtract current instead of adding
            if current_value < next_value:
                total += next_value - current_value
                i += 2
                continue #Skip normal addition below when necessary

        total += current_value
        i += 1

    print(total)

roman_numeral_conversion()