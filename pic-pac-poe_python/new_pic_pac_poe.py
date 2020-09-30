turn = 1
count = 0
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
game_won  = False
player = 'X'

def print_divider():
    print("-------------")
    
def print_board(board):
    print(" " + board[6] + " " + "|" + " " + board[7] + " " + "|" + " " + board[8])
    print_divider()
    print(" " + board[3] + " " + "|" + " " + board[4] + " " + "|" + " " + board[5])
    print_divider()
    print(" " + board[0] + " " + "|" + " " + board[1] + " " + "|" + " " + board[2])

def win_game():
    global player, board, game_won

    hor1 = [board[0], board[1], board[2]]
    hor2 = [board[3], board[4], board[5]]
    hor3 = [board[6], board[7], board[8]]
    diag1 = [board[0], board[4], board[8]]
    diag2 = [board[6], board[4], board[2]]
    ver1 = [board[0], board[3], board[6]]
    ver2 = [board[1], board[4], board[7]]
    ver3 = [board[2], board[5], board[8]]
    
    win_conditions = [hor1, hor2, hor3, diag1, diag2, ver1, ver2, ver3]
    print(hor1)
    for win in win_conditions:
        if win.count('X') == 3:
            game_won = True
            print(f'congrats {player} you win')
        elif win.count('O') == 3:
            game_won = True
            print(f'congrats {player} you win')
    get_move()

def get_move():
    global game_won
    while game_won == False:
        move()
        print_board(board)
        turn_switcher()
        win_game()
    
def turn_switcher():
    global turn, player
    turn *= -1
    if turn == 1:
        player = 'X'
    if turn == -1:
        player = 'O'

def move():
    global count, board, turn, player
    player_move = int(input('Please enter a square: '))
    if board[player_move-1] == 'X' or board[player_move-1] =='O':
        get_move()
    board[player_move-1] = player
    count += 1

def game():
    print_board(board)
    get_move()

game()