'''
Write a function called count_anagrams(words) that accepts a list of words (strings) and returns the number of different anagram classes in the list.

For example, for the input

['bacd', 'bcad', 'bcda', 'adf']
the correct output is 2.
'''


words = ['dog', 'cat', 'dog', 'tac', 'god', 'bird']

def count_anagrams(words):
    new_set = set()
    for word in words:
        ana = ''.join(sorted(word)) # sort each string in the words list in alpha order
        if ana not in new_set:
            new_set.add(ana)
    return len(new_set)

print(count_anagrams(words))