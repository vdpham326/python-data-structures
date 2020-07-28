volleyball_players = {'John Williams', 'Tom Jones', 'Jessica White', 'James Moore', 'Anne Davis', 'Lara Taylor', 'Conrad Anderson', 'Ronald Martin', 'Harry Thompson', 'Anne Wilson', 'Stephanie Lewis', 'Ted Garcia', 'Jane Walker', 'Paul Clark'}
basketball_players = {'John Robinson', 'Steven Clark', 'Jessica White', 'Andrew Rodiguez', 'James Moore', 'Sam Taylor', 'Conrad Anderson', 'James Martin', 'Ron Miller', 'Olivia Allen', 'Sophia King', 'Anne Wilson'}


diff_set_volley = volleyball_players.difference(basketball_players) #find all the people who are in volleyball but not in basketball
diff_set_basketball = basketball_players.difference(volleyball_players) #find all the people who are in basketball but not in volleyball


both_set = volleyball_players.intersection(basketball_players) #find people who are in both volley and basketball
both_cost = int(len(both_set) * 60) #cost when person is in both volleyball and basketball
volley_cost = int(len(diff_set_volley) * 50)
basketball_cost = int(len(diff_set_basketball) * 45)

total = both_cost + volley_cost + basketball_cost
print(total)