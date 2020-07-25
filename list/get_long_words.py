'''
Write a function named get_long_words(input_list, min_len). The function accepts a list of strings and returns a new list containing
only words at least as long as the minimum length provided as the second argument (min_len).

You can use the sample_words list in the template to test your function.
'''
sample_words = ['bird', 'carpet', 'bicycle', 'orange', 'floccinaucinihilipilification']


def get_long_words(input_list, min_len):
    new_words = [] 
    for word in input_list:
        if len(word) >= min_len:
            new_words.append(word)
    return new_words

print(get_long_words(sample_words, 5))
