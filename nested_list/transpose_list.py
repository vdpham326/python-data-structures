
def vertical_flip(input_list):
    new_list = []
    for i in range(len(input_list)):
        new_row = []
        for j in range(len(input_list[i])//2):
            #print(len(input_list[i])//2) = 2
            input_list[i][j], input_list[i][len(input_list[i]) - j - 1] = input_list[i][len(input_list[i]) - j - 1], input_list[i][j]
            new_row.append(input_list[i][j])
            #new_row.append(input_list[i][len(input_list[i]) - j - 1])
        new_list.append(new_row)
    return new_list            
        


sample_list = [
  ['a1', 'b1', 'c1', 'd1', 'e1'],
  ['a2', 'b2', 'c2', 'd2', 'e2'],
  ['a3', 'b3', 'c3', 'd3', 'e3']
]


print(vertical_flip(sample_list))
