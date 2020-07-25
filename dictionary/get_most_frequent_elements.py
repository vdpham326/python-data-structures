quotation = [
  "'Tis", "sweet", "and", "commendable", "in", "your", "nature", "Hamlet",
  "To", "give", "these", "mourning", "duties", "to", "your", "father",
  "But", "you", "must", "know", "your", "father", "lost", "a", "father",
  "That", "father", "lost", "lost", "his", "and", "the", "survivor", "bound",
  "In", "filial", "obligation", "for", "some", "term",
  "To", "do", "obsequious", "sorrow", "but", "to", "persever",
  "In", "obstinate", "condolement", "is", "a", "course",
  "Of", "impious", "stubbornness", "'tis", "unmanly", "grief"
]

def get_most_frequent_element(string_list):
    str = ''
    most = 0
    count = 0 # will count the num of appearance of a specific string
    dict = {} # dictionary that will hold the word as key and the number of time the word appear in the list
    for str in string_list:
        if str not in dict:
            dict[str] = 0
        dict[str] += 1
    
    highest = 0
    for key in dict:
        if dict[key] > highest:
            highest = dict[key]
            str = key
    return (str, highest)
    


#alternative solution

def get_most_frequent_element(string_list):
    counter = {}

    for word in string_list:
        counter[word] = counter.get(word, 0) + 1

    for k, v in counter.items():
        if v == max(counter.values()):
            return k,v

p