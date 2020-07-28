def count_letter_banks(words):
    count = 0
    a = set()
    for word in words:
        a.add(''.join(sorted(set(word))))
    return len(a)