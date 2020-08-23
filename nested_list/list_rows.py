'''
For each of the four applications, find and print the average score given to the podium finishers:

Average score: {average value for app1}
Average score: {average value for app2}
Average score: {average value for app3}
Average score: {average value for app4}

'''



hackathon_results = [
  [('HackKittens', 78), ('01011Brasil', 71), ('GoForCode', 65)],
  [('01011Brasil', 93 ), ('NullPointerException', 92), ('WeAreCode', 89)],
  [('FromIndiaWithCode', 87), ('MutexLovers', 86), ('HackKittens', 83)],
  [('WeAreCode', 97), ('HackKittens', 85), ('ThePythonists', 63)]
]


for application in hackathon_results:
    temp_score = 0
    for team in application:
        temp_score += team[1]
    print(f"Average score: {temp_score/len(application)}")