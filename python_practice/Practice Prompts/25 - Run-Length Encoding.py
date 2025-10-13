# Given a string like "aaabbcddd", return "a3b2c1d3".

def runlength_encoder(prompt):

    lower_string = str(prompt).lower().strip()

    temp_string_list = []
    current_count = 1

    for i, letter in enumerate(lower_string):

        if i < len(lower_string) - 1:

            if lower_string[i] == lower_string[i + 1]:
                current_count += 1
                
            else:
                temp_string_list.append(letter)
                temp_string_list.append(str(current_count))

                current_count = 1
        else:
            temp_string_list.append(letter)
            temp_string_list.append(str(current_count))
        
    return "".join(temp_string_list)

result = runlength_encoder("aabbbaa")      
print(result)