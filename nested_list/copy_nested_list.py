'''
Create a function named remove_negative(nested_list) that accepts a nested list of numbers as shown in the template code. The function should return a copy of the nested list with 
all the negative numbers removed.
'''


sample_numbers = [
  [34, -52, 349, 0, 32],
  [45, 245, 823, 1, 234, -358],
  [98, -234, -32, -324, -342, 543]
]

def remove_negative(nested_list):
    new_list = []
    for row in nested_list:
        new_row = []
        for number in row:
            if number >= 0:
                new_row.append(number)
        new_list.append(new_row)
    return new_list

print(remove_negative(sample_numbers))