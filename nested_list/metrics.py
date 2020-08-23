hackathon_results = [
  [('HackKittens', 78), ('01011Brasil', 71), ('GoForCode', 65)],
  [('01011Brasil', 93 ), ('NullPointerException', 92), ('WeAreCode', 89)],
  [('FromIndiaWithCode', 87), ('MutexLovers', 86), ('HackKittens', 83)],
  [('WeAreCode', 97), ('HackKittens', 85), ('ThePythonists', 63)]
]


count = 0
count_good_results = {} 

for application in hackathon_results:
    for team in application:
        name, score = team
        if score > 75:
            count_good_results[name] = count_good_results.get(name, 0) + 1
        

print(count_good_results)