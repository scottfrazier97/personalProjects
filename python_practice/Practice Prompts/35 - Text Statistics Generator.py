# Given a paragraph, return: 1) Word Count, 2) Unique Word Count 3) Average Word Length 4) Longest Word

def paragraph_stats(prompt):

    lower_string = str(prompt).lower().strip()

    invalid_chars = [".", ",", "'"]

    for char in invalid_chars:
        lower_string = lower_string.replace(char, "")

    clean_lower_string = lower_string.split()

    word_count = 0
    unique_words = set(clean_lower_string)
    word_lengths = 0
    longest_word = ""

    for word in clean_lower_string:

        word_count += 1
        word_lengths += len(word)
        
        if len(word) > len(longest_word):
            longest_word = word

    avg_word_length = round(word_lengths / len(clean_lower_string), 2)

    return word_count, len(unique_words), avg_word_length, longest_word

wcount, uniquewds, avglenv, longest = paragraph_stats("""In the heart of the city, the library stood as a beacon of knowledge and curiosity. 
    Students, researchers, and casual readers alike wandered its aisles, 
    searching for books that would expand their minds and transport them to different worlds. 
    The library hosted weekly events, including storytelling sessions for children, 
    lectures on history and science, and workshops on writing and literature. 
    Despite the hustle and bustle outside, inside the library there was a calm serenity, 
    where one could lose track of time amidst the pages of countless books. 
    Visitors often remarked that the scent of old pages and polished wood created 
    an atmosphere that was both comforting and inspiring, a reminder that learning 
    was a lifelong adventure.""")

print(f"Total count: {wcount}\nUnique count: {uniquewds}\nAverage length: {avglenv}\nLongest word: {longest}")