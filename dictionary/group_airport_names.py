'''
You are given a list of tuples storing information about airports. Each tuple consists of the airport's name and its number of runways.

Your task is to create a dictionary named runways which will group all airport names by the number of runways. In other words, the keys should represent the numbers of runways and the values should store 
lists of airport names.
'''


airport_runways = [
  ('Warsaw', 2),
  ('Vienna', 2),
  ('Frankfurt', 4),
  ('London Heathrow', 2),
  ('Fukuoka', 1),
  ('Madrid', 4)
]


runways = {}

for airport in airport_runways:
    name, num = airport
    if num not in runways:
        runways[num] = []
    runways[num].append(name)

print(runways)