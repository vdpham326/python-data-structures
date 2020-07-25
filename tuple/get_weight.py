'''
Write a function named get_weight_stats(list_a, list_b). The two arguments are lists with body weights expressed as float values. 
The template code presents an example of such lists. Both lists represent the weight values of the same people at two different points in time.

Your task is to analyze the weight values, element by element, and return a tuple with three counts: (the number of people who lost weight, the number 
of people with identical weight, and the number of people who gained weight).
'''
#use the zip() function
weight_2017 = [81.4, 67.8, 78.2, 64.5]
weight_2018 = [83.5, 65.7, 78.2, 68.9]

def get_weight_stats(list_a, list_b):
    lost, same, gain = 0, 0, 0
    for weight in zip(list_a, list_b):
        if weight[0] > weight[1]:
            lost += 1
        elif weight[0] < weight[1]:
            gain += 1
        else:
            same += 1
    return (lost, same, gain)