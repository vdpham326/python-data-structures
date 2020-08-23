'''
Implement another version of the hero_move_right(board) function. This time, when the hero stands in the rightmost column and wants to move right, put him in the leftmost column of the same row.

hero_move
'''


def hero_move_right(board):
  for i in range(len(board)):
    for j in range(len(board[i]) - 1):
      if board[i][j] == 'H' and board[i][j + 1] != 'x':
        board[i][j] = '-'
        board[i][j + 1] = 'H'
        return board
      elif board[i][j] == 'H' and board[i][j + 1] != 'x' and board[i][j+1] == len(board(i)):
        board[i][j + 1] = '-'
        board[i][0] = 'x'
        return board
  return board