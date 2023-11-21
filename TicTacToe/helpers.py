def draw_board(pos):
    board = (f"|{pos[1]}|{pos[2]}|{pos[3]}|\n"
             f"|{pos[4]}|{pos[5]}|{pos[6]}|\n"
             f"|{pos[7]}|{pos[8]}|{pos[9]}|")
    print(board)

def check_turn(turn):
  if turn % 2 == 0: return 'O'
  else: return 'X'

def check_for_win(pos):
  # Handle Horizontal Cases
  if   (pos[1] == pos[2] == pos[3]) \
    or (pos[4] == pos[5] == pos[6]) \
    or (pos[7] == pos[8] == pos[9]):
    return True
  # Handle Vertical Cases
  elif   (pos[1] == pos[4] == pos[7]) \
    or (pos[2] == pos[5] == pos[8]) \
    or (pos[3] == pos[6] == pos[9]):
    return True
  # Diagonal Cases
  elif (pos[1] == pos[5] == pos[9]) \
    or (pos[3] == pos[5] == pos[7]):
    return True
    
  else: return False