'''
Create a function called repeated_position(current_position, moves) that, for a given position (current_position) and a list of moves (moves), 
returns the first position in which the pawn finds itself for the second time (if such a position exists), or -1 if all positions occupied by the pawn are different.

You can use the function next_position(current_position, move) that was created in the previous exercise.
'''


def next_position(current_position, move):
  x, y = current_position
  if move == 'left':
    new_position = (x - 1, y)
  elif move == 'right': 
    new_position = (x + 1, y)
  elif move == 'up':
    new_position = (x, y + 1)
  else:
    new_position = (x, y - 1)
  return new_position

def repeated_position(current_position, moves):
    positions = set()
    positions.add(current_position)
    for move in moves: #loop over all the directions in the list called moves and add the position to the set
        np = next_position(current_position, move) #update current position 
        if np in positions:
            return np
        if np not in positions:
            positions.add(np) #add new position to the set    
        return -1
    
       
print(repeated_position((2, 0), ["up", "left", "up", "left", "down", "right", "up", "right", "up", "left"])) # expect (1, 1)
print(repeated_position((0, 1), ["up", "left", "up", "left", "down", "left", "up", "up"])) # expect -1
