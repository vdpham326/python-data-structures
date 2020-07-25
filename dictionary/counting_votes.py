'''
The mayor of a small town decided to change the town's name to attract more tourists. Three names were suggested: Screamer, Smackover, and Hazardville. The votes list contains all the citizens' votes. Your job is to:

Count the number of votes for each name and store the results in a variable named counted_votes.
Find the name with the most votes and print the following:
{name} is the winning name!

To solve the first part of the problem, use the code from the explanation. To solve the second part of the problem, iterate over the keys and values with counted_votes.items().
'''




votes = ['Screamer', 'Screamer', 'Hazardville', 'Smackover', 'Hazardville', 'Smackover', 'Screamer', 'Screamer', 
  'Hazardville', 'Smackover', 'Screamer', 'Screamer', 'Smackover', 'Smackover', 'Hazardville', 'Smackover', 
  'Hazardville', 'Smackover', 'Screamer', 'Smackover']


counted_votes = {}

for vote in votes:
    if vote not in counted_votes:
        counted_votes[vote] = 0
    counted_votes[vote] += 1


max_vote = 0
max_name = ''
for key, value in counted_votes.items():
    if value > max_vote:
        max_vote = value
        max_name = key

print(f'{max_name} is the winning name!')


    