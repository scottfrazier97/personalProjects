# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]

prefixes = ""

i = 0

for item in strs:

    if item[i] == strs[-1][i]:
        prefixes += item[i]
        i += 1

    else:
        if len(prefixes) > 0:
            print(f"Longest prefix: {prefixes}")
        else:
            print("No prefix found")