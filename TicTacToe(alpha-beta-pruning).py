# This is a 1 player version
import math


def draw_grid():
    global board

    print(" --- --- ---")
    for i in range(3):
        print("| " + str(board[i][0]) + " | " + str(board[i][1]) + " | " + str(board[i][2]) + " |")
        print(" --- --- ---")


def check_win(boards):
    global finished

    winner = ""

    # Check horizontal
    for i in range(3):
        if boards[0][i] == boards[1][i] == boards[2][i] and boards[0][i] != " ":
            finished = True
            winner = boards[0][i]

    # Check vertical
    for i in range(3):
        if boards[i][0] == boards[i][1] == boards[i][2] and boards[i][0] != " ":
            finished = True
            winner = boards[i][0]

    # Check diagonal
    if boards[0][0] == boards[1][1] == boards[2][2] and boards[1][1] != " " \
            or boards[0][2] == boards[1][1] == boards[2][0] and boards[1][1] != " ":
        finished = True
        winner = boards[1][1]

    # Check if empty
    space = 0
    for i in range(3):
        for j in range(3):
            if boards[i][j] == " ":
                space = space + 1

    # Check tie
    if space == 0 and winner == "":
        return "tie"
    else:
        return winner


def check_empty():
    global count, board

    empty = True
    while empty:

        if count % 2 != 0:  # Player O(Player)
            mark = "O"
            ret = check_input()

            # Check if empty
            if board[int(ret[0]) - 1][int(ret[1]) - 1] == " ":
                board[int(ret[0]) - 1][int(ret[1]) - 1] = mark
                empty = False
            else:
                print("The box was occupied, please choose again.")

        else:  # Player X(AI)
            mark = "X"
            bestscore = -math.inf
            bestmove = ""

            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "X"
                        score = minimax(board, 0, -math.inf, math.inf, False)
                        board[i][j] = " "
                        if score > bestscore:
                            bestscore = score
                            bestmove = (i, j)

            board[bestmove[0]][bestmove[1]] = mark
            empty = False


def check_input():
    # Check for the right input
    while True:
        x = input("Player O , what is your move?(e.g. 1,3) ").strip()
        cor = x.split(",")
        # Check if input is right
        if 4 > int(cor[0]) > 0 and 4 > int(cor[1]) > 0:
            return cor  # ["1","2"]
        else:
            print("The coordinates are not existed")


def minimax(boards, depth, alpha, beta, ismaximizing):
    result = check_win(boards)
    if result != "":
        if result == "X":
            return +100 - depth
        elif result == "O":
            return -100 + depth
        elif result == "tie":
            return 0

    if ismaximizing:

        bestscore = -math.inf
        for i in range(3):
            for j in range(3):
                if boards[i][j] == " ":
                    boards[i][j] = "X"
                    score = minimax(boards, depth + 1, alpha, beta, False)
                    boards[i][j] = " "
                    bestscore = max(score, bestscore)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return bestscore
    else:
        bestscore = math.inf
        for i in range(3):
            for j in range(3):
                if boards[i][j] == " ":
                    boards[i][j] = "O"
                    score = minimax(boards, depth + 1, alpha, beta, True)
                    boards[i][j] = " "
                    bestscore = min(score, bestscore)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return bestscore


# Variables
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
finished = False
o = 9

first = input("Who wants to go first? X:Computer O:Player ").upper()

if first == "X":
    count = 0
else:
    count = 1
    o = 10
# Game loop


draw_grid()

# Loop for 9 times maximum
while count < o:

    check_empty()

    draw_grid()

    result = check_win(board)
    if result == "X" or result == "O":
        print(result + " wins")
        break
    else:
        print(result)

    count += 1
