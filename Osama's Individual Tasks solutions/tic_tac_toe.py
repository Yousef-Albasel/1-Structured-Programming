def print_board(board):
    for row in board:
        print(row)

def check_win(board, symbol):
    # Check rows
    for row in board:
        if row.count(symbol) == 3:
            return True
    # Check columns
    for i in range(3):
        if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
            return True
    # Check diagonals
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    return False

def play_game():
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    players = ['x', 'O']
    current_player = players[0]
    while True:
        print_board(board)
        print(f"{current_player}'s turn")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if board[row][col] != '-':
            print("That cell is not avilable. choose again.")
            continue
        board[row][col] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        if '-' not in [cell for row in board for cell in row]:
            print_board(board)
            print("It's a tie!")
            break
        current_player = players[(players.index(current_player) + 1) % 2]

play_game()
