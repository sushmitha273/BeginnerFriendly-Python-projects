import random
from IPython.display import clear_output


def display_board(board):
    clear_output()
    print("   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]}  ")
    print(" ---------")
    print(f" {board[3]} | {board[4]} | {board[5]}  ")
    print(" ---------")
    print(f" {board[6]} | {board[7]} | {board[8]}  ")
    # print(" ---------")
    print("   |   |  ")


def choose_first():
    turn = random.randint(0, 1)
    if turn == 0:
        return "player1"
    else:
        return "player2"


def choose_mark(turn):
    mark = " "
    if not mark == "x" or mark == "o":
        mark = input(f'{turn} choose your mark? X or O').upper()
        if turn == "player1" and mark == "X" or turn == "player2" and mark == "O":
            return ["X", "O"]
        else:
            return ["O", 'X']


def space_check(board, pos):
    return board[pos] == " "


def choose_pos(board, turn):
    pos = -1
    while pos not in [0, 1, 2, 3, 4, 5, 6, 7, 8] or not space_check(board, pos):
        # if space_check(board,pos) or pos==-1:
        pos = int(input(f"{turn} Where you want to place your mark on the board? Choose between 0 to 9: "))
        # else:
        #     print("This position is already been filled please choose another position!!")
    return pos


def place_mark_on_pos(board, mark, pos):
    board[pos] = mark


def win_check(board, mark):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] == mark:
            return True
    return False


def tie_check(board):
    for i in range(0, len(board)):
        if space_check(board, i):
            return False
    return True


def replay():
    choise = input("Wanna replay the game? enter yes or no").lower()
    return choise == 'yes'


k = True
while True and k:

    board = [" "] * 9
    # display_board(board)

    turn = choose_first()
    print(f"{turn} will go first   ")
    player1_mark, player2_mark = choose_mark(turn)
    game_begin = (input("Ready to play the game? enter y or n: ")).lower()
    game_on = False
    if game_begin == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == "player1":
            display_board(board)
            position = choose_pos(board, turn)
            place_mark_on_pos(board, player1_mark, position)
            if win_check(board, player1_mark):
                display_board(board)
                print("Player 1 won")
                game_on = False
            else:
                if tie_check(board):
                    display_board(board)
                    print("Tie")
                    break
                else:
                    turn = "player2"
        else:
            display_board(board)
            position = choose_pos(board, turn)
            place_mark_on_pos(board, player2_mark, position)
            if win_check(board, player2_mark):
                display_board(board)
                print("Player 2 won")
                game_on = False
            else:
                if tie_check(board):
                    display_board(board)
                    print("Tie")
                    break
                else:
                    turn = "player1"
    if not replay():
        print("Thank u for playing the game. hope u had fun!!")
        # k=False
        break

# import random
# # from IPython.display import clear.output
# def display_board(board):
#     # clear_output()
#     print(f'   |     |  ')
#     # print(f'-------------')
#     print(f'{board[0]}  |  {board[1]}  |  {board[2]}')
#     print(f'-------------')
#     # print(f' |    |  ')
#     print(f'{board[3]}  |  {board[4]}  |  {board[5]}')
#     print(f'-------------')
#     print(f'{board[6]}  |  {board[7]}  |  {board[8]}')
#     # print(f'-------------')
#     print(f'   |     |  ')
# # board=['x','o',0,0,0,0,0,0,0]
# def choose_first():
#     flip=random.randint(0,1)
#     if flip==0:
#         return "player1"
#     else:
#         return "player2"
# def player_input(turn):
#     marker=" "
#     while not(marker=="X" or marker=="O"):
#         # player=choose_first()
#         marker=input(f"{turn} choose X or O: ").upper()
#         if turn=='player1' and marker=="X" or turn=="player2" and marker=="O":
#             return ["X","O"]
#         else:
#             return ["O","X"]
# def place_marker(board,marker,pos):
#     board[pos]=marker
# def win_check(board,mark):
#     wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
#     for win in wins:
#         if board[win[0]]==board[win[1]]==board[win[2]]==mark:
#             return True
#     return False
# def space_check(board,pos):
#     return board[pos]==" "
# def player_choice_pos(board,turn):
#     pos=-1
#     while pos not in [0,1,2,3,4,5,6,7,8] or not space_check(board,pos):
#         pos=int(input(f"{turn} Choose a position from 0 to 8: "))
#     return pos
# def replay():
#     choice=input("play again? Enter Yes or No").lower()
#     return choice=="yes"
# def full_board_check(board):
#     for i in range(0,len(board)):
#         if space_check(board,i):
#             return False
#     return True
# #  main program starts here
# k=True
# while True and k:
#     print("Welcome to Tic-Tac-Toe")
#     board = [" "] * 9
#     turn = choose_first()
#     print(turn + " will go first")
#     player1_marker, player2_marker = player_input(turn)
#     playgame = input("Ready to play? y or n: ").lower()
#     game_on = False
#     if playgame == 'y':
#         game_on = True
#     else:
#         game_on = False
#     while game_on:
#         if turn == 'player1':
#             display_board(board)
#             position = player_choice_pos(board,turn)
#             place_marker(board, player1_marker, position)
#             if win_check(board, player1_marker):
#                 display_board(board)
#                 print("player 1 won")
#                 game_on = False
#             else:
#                 if full_board_check(board):
#                     display_board(board)
#                     print("tie game")
#                     break
#                 else:
#                     turn = "player2"
#         else:
#             display_board(board)
#             position = player_choice_pos(board,turn)
#             place_marker(board, player2_marker, position)
#             if win_check(board, player2_marker):
#                 display_board(board)
#                 print("player 2 won")
#                 game_on = False
#             else:
#                 if full_board_check(board):
#                     display_board(board)
#                     print("tie game")
#                     break
#                 else:
#                     turn = "player1"
#     k=replay()

# place_mark_on_pos(board,plamark,pos)
