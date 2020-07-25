
'''
Three friends – Mike, John, and Tom – measured their jumps lengths in centimeters. We've stored their jump results in the template code. Create a dictionary named avg_results which will store the names as keys and their average 
jump lengths as values.
'''

jumps = [('Mike', 283), ('Mike', 317), ('Mike', 302), ('John', 305), ('John', 311), ('John', 297), ('John', 308), ('Tom', 341), ('Tom', 256)]

avg_results = {}
count_jumps = {}
sum_results = {}

for jump in jumps:
  name, result = jump
  sum_results[name] = sum_results.get(name, 0) + result #add up the values for each person (key)
  count_jumps[name] = count_jumps.get(name, 0) + 1 #count the number of jumps
  
for key, value in sum_results.items():
    avg_results[key] = value / count_jumps[key]  

print(avg_results)