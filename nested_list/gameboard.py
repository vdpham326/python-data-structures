'''
Create a function named is_board_correct(input_board) that accepts a game board in the format shown in the template code. 
The function should count the number of obstacles on the board (represented by 'x') and return True if there are exactly three obstacles. 
If there is any other number of obstacles, the function should return False.
You can use the example game boards in the template to test your code.

'''

def is_board_correct(input_board):
    count = 0
    for i in range(len(input_board)):
        for j in range(len(input_board[i])):
            if input_board[i][j] == 'x':
                count += 1
    if count == 3:
        return True
    return False


game_board = [
  ['-', '-', 'x', '-', '-'],
  ['-', '-', '-', '-', '-'],
  ['x', '-', '-', '-', '-'],
  ['-', '-', '-', 'x', '-']
]
incorrect_board = [
  ['-', 'x', 'x'],
  ['x', 'x', '-'],
  ['-', '-', '-']
]


print(is_board_correct(game_board))
print(is_board_correct(incorrect_board))