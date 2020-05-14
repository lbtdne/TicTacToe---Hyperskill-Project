# Define elements for drawing

bound_ = "---------"  # Top and bottom grid bounds

# Create a global variable that houses string of gameboard and any current play

board_ = str()  # Gameboard eg XOXOOX__X
play_ = []  # A player's chosen place to play X or Y
game_over = False
game_state = str()
who_turn = str()


# Define a function that begins the game and takes initial input

def start_board():
    global board_
    global who_turn
    board_ = "_________"  # Accepts input as 9 character str
    who_turn = "X"
    grid_draw(board_)


# Define a function to take a 9 length string and draw a grid

def grid_draw(x):
    row_1 = [x[i] for i in range(0, 3)]
    row_2 = [x[i] for i in range(3, 6)]
    row_3 = [x[i] for i in range(6, 9)]

    print(bound_)
    print("| " + row_1[0] + " " + row_1[1] + " " + row_1[2] + " " + " |")
    print("| " + row_2[0] + " " + row_2[1] + " " + row_2[2] + " " + " |")
    print("| " + row_3[0] + " " + row_3[1] + " " + row_3[2] + " " + " |")
    print(bound_)


# Define a function to check if an input coordinate is valid play given z as the input board.
# This will be used to validate user input during function call to take user's new move as input

def valid_play_finder(x, y, board):
    playable_ = True
    if y == 3:
        if board[x - 1] != "_":
            playable_ = False
    elif y == 2:
        if board[x + 2] != "_":
            playable_ = False
    elif y == 1:
        if board[x + 5] != "_":
            playable_ = False
    return playable_


# Define a function that takes coordinates from player for their move
# Then checks against board and sense to make sure it's valid


def move_accept(board):
    global play_
    while True:
        try:
            print("Enter the coordinates: ")
            coords_ = input()
            coords_ = coords_.split()
            if not ((0 < int(coords_[0]) <= 3) and (0 < int(coords_[1]) <= 3)):
                print("Coordinates should be from 1 to 3!")
            elif not valid_play_finder(int(coords_[0]), int(coords_[1]), board):
                print("This cell is occupied! Choose another one!")
            else:
                play_ = coords_
                return
        except ValueError:
            print("You should enter numbers!")


# Create a function that takes the users move and plays their move

def make_play(move, board):
    global board_
    global who_turn
    board_list = [i for i in board]
    x_coord = int(move[0])
    new_board = str()
    if move[1] == "3":
        board_list[x_coord - 1] = who_turn
    elif move[1] == "2":
        board_list[x_coord + 2] = who_turn
    elif move[1] == "1":
        board_list[x_coord + 5] = who_turn
    for i in board_list:
        new_board = new_board + str(i)
    board_ = new_board
    if who_turn == "X":
        who_turn = "O"
    else:
        who_turn = "X"


def analyse_board(all_in):
    global game_state
    global game_over
    # Take input string and convert to 3 x 3 matrix, and separate rows and columns and diagonals
    row_1 = [all_in[i] for i in range(0, 3)]
    row_2 = [all_in[i] for i in range(3, 6)]
    row_3 = [all_in[i] for i in range(6, 9)]

    col_1 = [all_in[i] for i in range(0, 9, 3)]
    col_2 = [all_in[i] for i in range(1, 9, 3)]
    col_3 = [all_in[i] for i in range(2, 9, 3)]

    dia_1 = [all_in[0], all_in[4], all_in[8]]
    dia_2 = [all_in[2], all_in[4], all_in[6]]

    grid_rows = [row_1, row_2, row_3]  # List of rows for iteration
    grid_cols = [col_1, col_2, col_3]  # List of columns for iteration
    grid_dias = [dia_1, dia_2]  # List of diagonals for iteration

    # Create booleans for final assessment of game state
    x_win = False
    o_win = False
    imposs_ = False

    #  Check for three in a row, X first then O

    # X wins
    for part in grid_rows:
        if part[0] == part[1] == part[2] == "X":
            x_win = True
        else:
            x_win = x_win

    # O wins
    for part in grid_rows:
        if part[0] == part[1] == part[2] == "O":
            o_win = True
        else:
            o_win = o_win

    # Check for three in a col, X first then O
    # X wins
    for part in grid_cols:
        if part[0] == part[1] == part[2] == "X":
            x_win = True
        else:
            x_win = x_win

    # O wins
    for part in grid_cols:
        if part[0] == part[1] == part[2] == "O":
            o_win = True
        else:
            o_win = o_win

    # Check for three in a diag, X first then O
    # X wins
    for part in grid_dias:
        if part[0] == part[1] == part[2] == "X":
            x_win = True
        else:
            x_win = x_win

    # O wins
    for part in grid_dias:
        if part[0] == part[1] == part[2] == "O":
            o_win = True
        else:
            o_win = o_win

    # Check for impossible game due to too many turns
    x_plays = 0
    o_plays = 0
    for part in grid_rows:
        for play in part:
            if play == "X":
                x_plays += 1
            elif play == "O":
                o_plays += 1

    if abs(x_plays - o_plays) >= 2:
        imposs_ = True

    # Calculate game_state

    if x_win and o_win:
        game_state = "Impossible"
        game_over = True
    elif o_win:
        game_state = "O wins"
        game_over = True
    elif x_win:
        game_state = "X wins"
        game_over = True
    elif imposs_:
        game_state = "Impossible"
        game_over = True
    elif "_" in all_in:
        game_state = "Game not finished"
    else:
        game_state = "Draw"
        game_over = True

    if game_over:
        print(game_state)


start_board()  # Start the game
while not game_over:
    move_accept(board_)  # Accept a player's move
    make_play(play_, board_)  # Make the player's move
    grid_draw(board_)  # Draw the new board
    analyse_board(board_)  # Check for a winner now

# Now I need to analyse the board for wins/losses/draws


# # Draw complete grid
#
# print(bound_)
# print("| " + row_1[0] + " " + row_1[1] + " " + row_1[2] + " " + " |")
# print("| " + row_2[0] + " " + row_2[1] + " " + row_2[2] + " " + " |")
# print("| " + row_3[0] + " " + row_3[1] + " " + row_3[2] + " " + " |")
# print(bound_)
# print(game_state)
