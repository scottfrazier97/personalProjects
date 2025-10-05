#Given a list of words, return a dict mapping each word → its length

words = ["cat", "dog", "cat"]

tracker = {}

for word in words:

    tracker[word] = len(word)

print(tracker)

#Pythonic:
# def word_lengths(words):
#     return {word: len(word) for word in words}