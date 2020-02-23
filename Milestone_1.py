def display_board(board):
    print("\n"*100)
    display = f"  {board[7]}  |  {board[8]}  |  {board[9]}  \n-----------------\n  {board[4]}  |  {board[5]}  |  {board[6]}  \n-----------------\n  {board[1]}  |  {board[2]}  |  {board[3]}  "
    return(display)

def player_input():
    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Player one, choose X or O: ")
    player1 = marker
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    return (player1, player2)

def player_choice(board, player_marker):
    choosed_num = 0
    while ((choosed_num not in board) or (choosed_num in ["X", "O"])):
        choosed_num = input("Choose your position: ")
    board[int(choosed_num)] = player_marker
    return display_board(board)

def is_winner(board, player):
    return(board[1] == board [2] == board[3] == player or
           board[4] == board [5] == board[6] == player or
           board[7] == board [8] == board[9] == player or
           board[7] == board [4] == board[1] == player or
           board[8] == board [5] == board[2] == player or
           board[9] == board [6] == board[3] == player or
           board[7] == board [5] == board[3] == player or
           board[9] == board [5] == board[1] == player)

def is_tie(board):
    for i in range(0,10):
        if board[i] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if i == 9:
                return True
        else:
            return False

def replay():
    play_again = True
    while(play_again):
        ask_player = input("Do You Want To Play Again? Y/N ")
        if ask_player == "Y":
            play_again = False
            return True
        elif ask_player == "N":
            play_again = False
            return False
        
play = True

while play :
    board_init = ["#", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    print(display_board(board_init))
    player1, player2 = player_input()
    turn = player1
    gameOn = True
    while (gameOn):
        if turn == player1:
            turn = player2
            print(player_choice(board_init, player1))
            if is_winner(board_init, player1):
                print("Player 1 wins!")
                gameOn = False
                play = replay()
            if is_tie(board_init):
                print("Tie Game!")
                gameOn = False
                play = replay()
                break
        else:
            turn = player1
            print(player_choice(board_init, player2))
            if is_winner(board_init, player2):
                print("Player 2 wins!")
                gameOn = False
                play = replay()
            if is_tie(board_init):
                print("Tie Game!")
                gameOn = False
                play = replay()
                break

    
        
    
        


    
