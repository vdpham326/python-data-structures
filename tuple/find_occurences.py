'''
Write the function find_occurences(text, letters) that, given a text and a list of letters, will find all occurences of the given letters, regardless of their case, in the text. The function should return the list of tuples of the form (index, letter), where index is the index of the letter in the text and letter is the letter from letters.

For example the function find_occurences('To be or not to be', ['e', 't']) should return the list [(0, 'T'), (4, 'e'), (11, 't'), (13, 't'), (17, 'e')].

To check if a given character is present in letters, you can use:

if character.lower() in letters:
When adding character to a list, don't lower the character:

list.append((i, character))
Also, it's a good idea to use an enumerate() function in your solution.
'''

def find_occurences(text, letters):
    new_list = []
    for i, character in enumerate(text):
        if character.lower() in letters:
            new_list.append((i, character))
    return new_list 


#find_occurences('To be or not to be', ['e', 't'])
print(find_occurences('To be or not to be', ['e', 't']))