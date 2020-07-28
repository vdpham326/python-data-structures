'''
Write a function named check_words(word1, word2) that accepts two strings and checks if we can create one of these strings using the letters from t
he other string (using each letter as many times as we need to). The function should return True if we can create word1 from the letters in word2 or if we can create word2 from the letters in word1. Otherwise, it should return False.

'''


def check_words(word1, word2):
    new_word1 = set(word1)
    new_word2 = set(word2)
    if new_word1 >= new_word2 or new_word1 <= new_word2 or new_word2 >= new_word1 or new_word2 <= new_word1:
        return True