

# gameboard
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if game is still going
game_still_going = True


# who won
winner = None

# whos turn iss it


person = input('Enter player 1 name: ')
person = input('Enter player 2 name:')
player_choice = input('Chose Who to start! (X or O): ').upper()
current_player = player_choice

print('Hello', person, "it's time to face your fears")


def play_game():

    display_board()

    who_starts()
    while game_still_going:

        handle_turn(player_choice)

        check_if_game_over()

        flip_player()

# end game
    if winner == "X" or winner == "O":
        print(winner + " won")
    elif winner is None:
        print("Tie")


def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " +
          board[2] + " Board No Reference   1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " +
          board[5] + "                      4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " +
          board[8] + "                      7 | 8 | 9")
    print("\n")


def handle_turn(player_choice):
    print(player_choice + "'s turn.")
    position = input("Choose position from 1 - 9:")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose position from 1 - 9:")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there.Go Again")
    board[position] = player_choice
    display_board()


def who_starts():
    if player_choice == "X":
        return True
    else:
        return False


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    global winner
    # check row
    row_winner = check_row()
    # check column
    column_winner = check_column()
    # check diagonal
    diagonal_winner = check_diagonal()
    # get winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_row():
    global game_still_going
    # if it has the same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board(3)
    elif row_3:
        return board(6)
    else:
        return None


def check_column():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board(1)
    elif column_3:
        return board(2)
    else:
        return None


def check_diagonal():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board(2)
    else:
        return None


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False


def flip_player():
    global player_choice
    if player_choice == "X":
        player_choice = "O"
    elif player_choice == "O":
        player_choice = "X"


play_game()
