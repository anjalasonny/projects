from helpers import draw_board, check_turn, check_for_win
import os

pos = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}

playing, complete = True, False
turn = 0
prev_turn = -1
while playing:
    # Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(pos)
    print("Player " + str((turn % 2) +1 ) + "'s turn: Pick your pos or press q to quit")
    if prev_turn == turn:
      print("Invalid pos selected, please pick another.")
    prev_turn = turn

    choice = input()
    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in pos:
      # Check if the pos is already taken.
      if not pos[int(choice)] in {"X", "O"}:
        turn += 1
        pos[int(choice)] = check_turn(turn)
      
    if check_for_win(pos): playing, complete = False, True
    if turn > 8: playing = False

    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(pos)
    # If there was a winner, say who won
    if complete:
        if check_turn(turn) == 'X': print("Player 1 Wins!")
        else: print("Player 2 Wins!")
    else: 
    # Tie Game
        print("No Winner")
    
    print("Thanks for playing!") 