words = ['gallery', 'recasts', 'casters', 'marine', 'bird', 'largely', 'actress', 'remain', 'allergy']

def find_anagrams(list):
    new = {}
    #key should store strings from input list with letters sorted alphabetically
    for word in list:
        key = ''.join(sorted(word))
        if key not in new:
            new[key] = [] #set the key in alphabet order and equal to an empty list for value 
        new[key].append(word)
    #value should contain a list of words from the input list which are anagrams for the given key
    return new


#alternative method using get() method

def find_anagrams2(list):
    new = {}
    #key should store strings from input list with letters sorted alphabetically
    for word in list:
        key = ''.join(sorted(word))
        new[key] = new.get(key, []) + [word]
    return new


#print(''.join(sorted(words[0])))

print(find_anagrams2(words))