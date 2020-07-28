'''
Create an all_players set and a new_players set. Then, count the number of elements in these sets and print:

There are {} players using the hall, {} of which are new players.
'''


volleyball_players = {'John Williams', 'Tom Jones', 'Jessica White', 'James Moore', 'Anne Davis', 'Lara Taylor', 'Conrad Anderson', 'Ronald Martin', 'Harry Thompson', 'Anne Wilson', 'Stephanie Lewis', 'Ted Garcia', 'Jane Walker', 'Paul Clark'}
basketball_players = {'John Robinson', 'Steven Clark', 'Jessica White', 'Andrew Rodiguez', 'James Moore', 'Sam Taylor', 'Conrad Anderson', 'James Martin', 'Ron Miller', 'Olivia Allen', 'Sophia King', 'Anne Wilson'}
football_players = {'Liam Boss', 'Emma Lees', 'Amelia Cooper', 'William Howard', 'Oliver Harris', 'Alexander Perry', 'Andrew Rodiguez', 'James Moore', 'Michael Long', 'Conrad Anderson', 'Emily Young', 'Samuel Bennett', 'Chloe Richardson', 'Sam Taylor', 'Jackson Perez', 'Charlotte Wright', 'David Scott', 'James Moore', 'Oliver Ward', 'Henry Rogers', 'John Harris', 'Victoria Smith', 'Harper Johnson', 'Joseph Allen', 'Nora Brown'}

#find all players in football who are not in volley and basketball
new_players = football_players - (volleyball_players | basketball_players)
all_players = new_players | ( volleyball_players | basketball_players)


print(f'There are {len(all_players)} players using the hall, {len(new_players)} of which are new players.')