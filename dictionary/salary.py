salaries_2017 = {'Anna': 4000, 'Mark': 5000, 'Jane': 5500, 'John': 3000}

salaries_2018 = salaries_2017.copy()

for salary in salaries_2018:
  salaries_2018[salary] = int(salaries_2018[salary] * 1.10)
  
print(salaries_2017)
print(salaries_2018)