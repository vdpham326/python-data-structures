'''
Create a list named averages that will store three elements:

The average application score among all winners.
The average application score among all runners-up.
The average application score among all third-place finishers.

First, create a nested loop in which you'll add all application scores to the respective elements in the averages variable.

Then, create a simple loop through the averages list and divide each element by 4.
'''


hackathon_results = [
  [('HackKittens', 78), ('01011Brasil', 71), ('GoForCode', 65)],
  [('01011Brasil', 93 ), ('NullPointerException', 92), ('WeAreCode', 89)],
  [('FromIndiaWithCode', 87), ('MutexLovers', 86), ('HackKittens', 83)],
  [('WeAreCode', 97), ('HackKittens', 85), ('ThePythonists', 63)]
]

averages = [0, 0, 0] # first, second, third place

for i, application in enumerate(hackathon_results):
    for j, value in enumerate(application):
        averages[j] += value[1]

for i, average in enumerate(averages):
    averages[i] = average / 4


print(averages)
