restaurant_customers = {
  'John Steven': (10, 'still waiting'),
  'Jane Black': (5, 'still waiting'),
  'Mark Dawson': (15, 'got the food :)'),
  'Janet Roberts': (30, 'left without eating :('),
  'John Parker': (22, 'still waiting'),
  'Anne Edwards': (18, 'got the food :)'),
  'Mary Rogers': (7, 'got the food :)'),
  'Emma Reed': (35, 'got the food :)'),
  'Sophia Steven': (25, 'still waiting'),
  'Amelia Cook': (32, 'still waiting'),
  'John Scott': (15, 'still waiting'),
  'George Famous': (20, 'still waiting'),
  'Jack Baker': (38, 'got the food :)')
}

count = 0
for key, value in restaurant_customers.items():
    if value[0] >= 20 and value[1] == 'still waiting' or value[1] == 'left without eating :(':
        restaurant_customers[key] = (value[0], 'left without eating :(')
        count += 1
    # if value[1] == 'left without eating :(':
    #     count += 1
    
    
print(f'{count} customers left')
