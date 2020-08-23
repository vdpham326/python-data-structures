'''
You are given hackathon_teams nested list that contains only team names. We now need to modify this list to store an abbreviated name for each team. Let's shorten each team name to its first five letters and add a dot (.).

For instance: 'HackKittens' should become 'HackK.'

'''



hackathon_teams = [
  ['HackKittens', '01011Brasil', 'GoForCode'],
  ['01011Brasil', 'NullPointerException', 'WeAreCode'],
  ['FromIndiaWithCode', 'MutexLovers', 'HackKittens'],
  ['WeAreCode', 'HackKittens', 'ThePythonists']
]

for i in range(len(hackathon_teams)):
    for j in range(len(hackathon_teams[i])):
        team_name = hackathon_teams[i][j]
        hackathon_teams[i][j] = team_name[:5] + '.'
print(hackathon_teams)