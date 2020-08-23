import copy


def copy_all_caps(nested_list):
    new_list = []
    for row in nested_list:
        new_row = []
        for val in row:
            new_row.append(val.upper())
        new_list.append(new_row)
    return new_list

hackathon_results = [
  ['HackKittens', '01011Brasil', 'GoForCode'],
  ['01011Brasil', 'NullPointerException', 'WeAreCode'],
  ['FromIndiaWithCode', 'MutexLovers', 'HackKittens'],
  ['WeAreCode', 'HackKittens', 'ThePythonists']
]

print(copy_all_caps(hackathon_results))



