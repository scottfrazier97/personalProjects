# Count all words in a paragraph excluding common stop words like “the”, “a”, “and”.

def word_frequency(sentence):

    from collections import Counter

    sentence_clean = str(sentence).strip().lower().split(" ")

    stop_words = set(["a", "an", "the", "and", "but", "in", "on", "of", "is", "it"])

    new_list_non_stop = [word for word in sentence_clean if word not in stop_words]
    
    return Counter(new_list_non_stop)

result = word_frequency("Blah blah blah I am typing random words and it is so much fun but I am out of space")
{print(k,v) for k,v in result.items()}