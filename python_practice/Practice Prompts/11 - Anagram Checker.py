#Given two strings, return True if one is an anagram of the other.
#Approach: 
#   1) Get lengths of both words
#   2) Track count of each letter

#Key point: Python compares key:value pairs, not insertion order between the dictionaries. Pre-emptive sorting not necessary.

def anagram_checker(word1, word2):

    word1_new = list(word1)
    word2_new = list(word2)

    tracker1 = {}
    tracker2 = {}

    if len(word1) == len(word2):
        for x in word1_new:
            if x not in tracker1:
                tracker1[x] = 1
            else:
                tracker1[x] += 1

        for y in word2_new:
            if y not in tracker2:
                tracker2[y] = 1
            else:
                tracker2[y] += 1

        if tracker1 == tracker2:
            print("Anagram")
        else:
            print("Not an anagram")

    else:
        print("Not an anagram")



anagram_checker("listen", "silent")
        

## !!!SUPER-ULTRA-MEGA-PYTHONIC VERSION!!!

# from collections import Counter

# def anagram_checker(word1, word2):
#     return Counter(word1) == Counter(word2)

# print(anagram_checker("fried", "fired"))  # True
# print(anagram_checker("hello", "world"))  # False
