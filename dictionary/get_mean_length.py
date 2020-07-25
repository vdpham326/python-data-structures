titles = {2016: 'Running To the Moon', 2008: 'When we are naughty', 2017: 'On the Beach'}

def get_mean_length(input_dict):
    sum = 0
    for value in input_dict.values():
       sum += len(value)
    return sum / len(input_dict)

print(get_mean_length(titles)) 