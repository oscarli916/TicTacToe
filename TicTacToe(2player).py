# indicator = {
#     0:" ",
#     1:"X",
#     2:"O"
# }

# This is a 2 player version


def draw_grid():
    global board

    print(" --- --- ---")
    for i in range(3):
        print("| " + str(board[i][0]) + " | " + str(board[i][1]) + " | " + str(board[i][2]) + " |")
        print(" --- --- ---")


def check_win(board):
    global finished
    # Check if column and row win
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            print("Player " + str(board[0][i]) + " win")
            finished = True

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            print("Player " + str(board[i][0]) + " win")
            finished = True

    # Check diagonal win
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != " " \
            or board[0][2] == board[1][1] == board[2][0] and board[1][1] != " ":
        print("Player " + str(board[1][1]) + " win")
        finished = True


# Variables
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

# Game loop

finished = False
count = 0

draw_grid()

# Loop for 9 times maximum
while not finished and count < 9:
    if count % 2 == 0:
        num = 1
        mark = "X"
    else:
        num = 2
        mark = "O"

    # Check for empty
    empty = True
    while empty:

        # Check for the right input
        while True:
            x = input("Player " + str(num) + " , what is your move?(e.g. 1,3) ").strip()
            cor = x.split(",")
            # Check if input is right
            if 4 > int(cor[0]) > 0 and 4 > int(cor[1]) > 0:
                break
            else:
                print("The coordinates are not existed")

        # Check if empty
        if board[int(cor[0]) - 1][int(cor[1]) - 1] == " ":
            board[int(cor[0]) - 1][int(cor[1]) - 1] = mark
            empty = False
        else:
            print("The box was occupied, please choose again.")

    draw_grid()

    check_win(board)

    count += 1

if not finished:
    print("It is a tie.")
