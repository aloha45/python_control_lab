def game():

    turn = 'X'
    count = 0
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    game_won  = False

    while game_won == False:
        def print_divider():
            print("-------------")
        def PrintBoard(board):
            print(" " + board[6] + " " + "|" + " " +
                board[7] + " " + "|" + " " + board[8])
            print_divider()
            print(" " + board[3] + " " + "|" + " " +
                board[4] + " " + "|" + " " + board[5])
            print_divider()
            print(" " + board[0] + " " + "|" + " " +
                board[1] + " " + "|" + " " + board[2])
        
        def player_move():
            print('hi')
            global count 
            count += 1

        def my_decorator(func):
            def wrap_function():
                print('----------------------')
                func()
                print('----------------------')
            return wrap_function

        @my_decorator
        def welcome():
            print("Let's play Py-Pac-Poe!")

        @my_decorator
        def player_turn():
            print(f"It is {player_turn}'s turn")

  # winning_combos = {
  #   [a1, a2, a3], 
  #   [a1, b1, c1], 
  #   [b1, b2, b3], 
  #   [c1, c2, c3], 
  #   [a2, b2, c2], 
  #   [a3, b3, c3], 
  #   [a1, b2, c3], 
  #   [a3, b2, c1]
  # }

    PrintBoard(board) 
    welcome()
    player_turn()

game()