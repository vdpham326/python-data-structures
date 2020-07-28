'''
Write a function named count_unique_letters(word) that accepts a string argument and returns the number of unique letters (characters) in the word.

'''

def count_unique_letters(word):
    set_word = set(word)
    return len(set_word)