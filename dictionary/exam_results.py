'''
Create a function named get_results_range(result_dict) that accepts a dictionary (as shown in the template code) and returns the difference between 
the best and worst exam results. The results are integers between 0 and 100.
'''

exam_results = {
  'Dominic Vargas': 67,
  'Marion Riley': 89,
  'Candice White': 45,
  'Doreen Goodwin': 82,
  'Janet Hunter': 98,
  'Jaime Page': 32,
  'Neil Fernandez': 76,
  'Jana Frank': 28,
  'Adrienne Perkins': 98,
  'Rosa Mccarthy': 34
}

def get_results_range(result_dict):
    worst, best = 0, 0
    for score in result_dict.values():
        if score < worst:
            worst = score
        if score > best:
            best = score
    return best - worst