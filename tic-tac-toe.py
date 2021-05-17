from IPython.display import clear_output
import random

def display_board(a, b):
    clear_output()
    print('Available      TIC TAC TOE\n  moves  \n')
    print('  '+a[1]+'|'+a[2]+'|'+a[3]+'           '+b[1]+'|'+b[2]+'|'+b[3])
    print('  -----           -----')
    print('  '+a[4]+'|'+a[5]+'|'+a[6]+'           '+b[4]+'|'+b[5]+'|'+b[6])
    print('  -----           -----')
    print('  '+a[7]+'|'+a[8]+'|'+a[9]+'           '+b[7]+'|'+b[8]+'|'+b[9])

def choose_marker():
    while True:
        choose = input("Player 1, choose your marker: 'X or 'O':").upper()
        if choose == 'X' or choose == 'O':
                Player1 = choose
                break
        else:
            print("Please enter a valid marker.")
            continue
    if Player1 == 'X':
        Player2 = 'O'
    else:
        Player2 = 'X'
    return (Player1, Player2)

def goes_first():
    a = random.randint(1,2)
    if a == 1:
        return 'Player1'
    else:
        return 'Player2'
        
def choose_position(name):
    while True:
        position = input(f'{name} choose your position:')
        if position in str([1,2,3,4,5,6,7,8,9]) and board[int(position)] == ' ':
            return position
            break
        else:
            print('Please enter a valid position.')
            continue
            
def mark_board(available, board, marker, position):
    board[int(position)] = marker
    available[int(position)] = ' '
    
def win_check(board, marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
    (board[4] == marker and board[5] == marker and board[6] == marker) or
    (board[7] == marker and board[8] == marker and board[9] == marker) or 
    (board[1] == marker and board[4] == marker and board[7] == marker) or 
    (board[2] == marker and board[5] == marker and board[8] == marker) or 
    (board[3] == marker and board[6] == marker and board[9] == marker) or 
    (board[1] == marker and board[5] == marker and board[9] == marker) or 
    (board[3] == marker and board[5] == marker and board[7] == marker))
    
def board_full(board):
    return ' ' not in board[1:]
    
def replay():
    a = input("Play again? 'Y' or 'N':").upper()
    return a == 'Y'
    
available = [str(i) for i in range(10)]
board = [' '] * 10
print('Welcome to TIC TAC TOE!')

while True:
    Player1_marker, Player2_marker = choose_marker()
    turn = goes_first()
    print('For this round '+turn, 'will go first!')
    game_on = True
    input('Hit enter to cotinue')
    while game_on:
        if turn == 'Player1':
            display_board(available, board)
            position = choose_position(turn)
            mark_board(available, board, Player1_marker, position)
            if win_check(board, Player1_marker):
                display_board(available, board)
                print('\nPlayer 1 wins!!')
                game_on = False
            else:
                if board_full(board):
                    display_board(available, board)
                    print("It's a tie!")
                    game_on  = False
                else:
                    turn = 'Player2'
        else:
            display_board(available, board)
            position = choose_position(turn)
            mark_board(available, board, Player2_marker, position)
            if win_check(board, Player2_marker):
                display_board(available, board)
                print('\nPlayer 2 wins!!')
                game_on = False
            else:
                if board_full(board):
                    display_board(available, board)
                    print("\nIt's a tie!")
                    game_on  = False
                else:
                    turn = 'Player1'
    
    available = [str(i) for i in range(10)]
    board = [' '] * 10
    
    if not replay():
        print('\nThank you for playing.')
        break
