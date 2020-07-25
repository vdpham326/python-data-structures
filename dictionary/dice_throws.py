'''Two distinct dice (e.g., blue and red) where rolled a few times. Each time we put the result in the tuple as (first_dice, second_dice).

Create a dictionary named results which will store the count of how many times a given combination was thrown.
'''

dice_throws = [(4, 3), (5, 6), (1, 3), (4, 3), (5, 5), (5, 6), (1, 3), (4, 3)]

results = {} #store the count of how many times a given combination was thrown.

for dice in dice_throws:
    results[dice] = results.get(dice, 0) + 1


print(results)
