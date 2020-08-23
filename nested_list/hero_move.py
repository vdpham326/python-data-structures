'''
Create a function named hero_move_down(board) that accepts a game board in the format shown in the template code, moves the hero ('H') one field down and returns the modified board. Do not move the hero if the new field is occupied by an obstacle ('x') or is outside the game board.
'''
def hero_move_down(board):
    for i in range(len(board)):
        for j in range(len(board[i]) -1):
            if board[i][


game_board = [
  ['-', '-', 'x', '-', '-'],
  ['-', 'H', '-', '-', '-'],
  ['x', '-', '-', '-', '-'],
  ['-', '-', '-', 'x', '-']
]

