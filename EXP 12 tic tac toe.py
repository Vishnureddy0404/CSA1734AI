def print_board(board):
    """Prints the current board state."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Checks if the player has won."""
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    """Checks if the board is full."""
    for row in board:
        if " " in row:
            return False
    return True

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")

        # Get user input for row and column
        while True:
            try:
                row = int(input("Enter row number (1-3): ")) - 1
                col = int(input("Enter column number (1-3): ")) - 1
                if row in range(3) and col in range(3) and board[row][col] == " ":
                    break
                else:
                    print("Invalid input. Please enter again.")
            except ValueError:
                print("Invalid input. Please enter again.")

        # Place player's move on the board
        board[row][col] = player

        # Check for winner
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check if board is full
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch turn to the other player
        turn += 1

if __name__ == "__main__":
    main()
