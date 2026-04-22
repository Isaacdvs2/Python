from random import randrange

def display_board(board):
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(row[0], row[1], row[2]))
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    while True:
        move = input("Enter your move (1-9): ")

        if not move.isdigit():
            print("Invalid input. Enter a number.")
            continue

        move = int(move)

        if move < 1 or move > 9:
            print("Number must be between 1 and 9.")
            continue

        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] in ['X', 'O']:
            print("Square already taken.")
            continue

        board[row][col] = 'O'
        break


def make_list_of_free_fields(board):
    free = []

    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', 'O']:
                free.append((r, c))

    return free


def victory_for(board, sign):
    # rows
    for row in board:
        if all(cell == sign for cell in row):
            return True

    # columns
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True

    # diagonals
    if all(board[i][i] == sign for i in range(3)):
        return True

    if all(board[i][2 - i] == sign for i in range(3)):
        return True

    return False


def draw_move(board):
    free = make_list_of_free_fields(board)

    if free:
        move = free[randrange(len(free))]
        board[move[0]][move[1]] = 'X'


# --- GAME LOOP ---

board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
]

while True:
    display_board(board)

    # User's move
    enter_move(board)

    if victory_for(board, 'O'):
        display_board(board)
        print("You win!")
        break

    if not make_list_of_free_fields(board):
        display_board(board)
        print("It's a tie!")
        break

    # Computer's move
    draw_move(board)

    if victory_for(board, 'X'):
        display_board(board)
        print("Computer wins!")
        break

    if not make_list_of_free_fields(board):
        display_board(board)
        print("It's a tie!")
        break