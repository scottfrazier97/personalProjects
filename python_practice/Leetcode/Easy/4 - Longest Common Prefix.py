# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = ""

    # loop over character positions in the first word
    for i in range(len(strs[0])):
        char = strs[0][i]

        # check this character against all the other words
        for word in strs[1:]:
            # if index out of range or mismatch → stop
            if i >= len(word) or word[i] != char:
                return prefix

        # if no mismatch, add the character to the prefix
        prefix += char

    return prefix


# Examples
print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"])) 



