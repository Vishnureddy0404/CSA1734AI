import math

def print_board(board):
    """Prints the current board state."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there is a winner or if the board is full (tie)."""
    for row in board:
        if all(cell == 'X' for cell in row):
            return 'X'
        elif all(cell == 'O' for cell in row):
            return 'O'
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 'X'
        elif all(board[row][col] == 'O' for row in range(3)):
            return 'O'
    if all(board[i][i] == 'X' for i in range(3)):
        return 'X'
    elif all(board[i][i] == 'O' for i in range(3)):
        return 'O'
    if all(board[i][2-i] == 'X' for i in range(3)):
        return 'X'
    elif all(board[i][2-i] == 'O' for i in range(3)):
        return 'O'
    # Check if board is full
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return 'Tie'
    return None

def minimax(board, depth, alpha, beta, is_maximizing):
    """Minimax algorithm function with Alpha-Beta pruning."""
    result = check_winner(board)
    if result is not None:
        if result == 'X':
            return -1
        elif result == 'O':
            return 1
        else:  # Tie
            return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break  # Beta cut-off
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break  # Alpha cut-off
        return best_score

def get_best_move(board):
    """Returns the best move for the AI using minimax with Alpha-Beta pruning."""
    best_move = None
    best_score = -math.inf
    alpha = -math.inf
    beta = math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, alpha, beta, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
                alpha = max(alpha, best_score)
    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    turn = 'X'  # Player X starts the game

    while True:
        print_board(board)
        
        # Human player's turn
        if turn == 'X':
            while True:
                try:
                    row = int(input("Enter row number (1-3): ")) - 1
                    col = int(input("Enter column number (1-3): ")) - 1
                    if row in range(3) and col in range(3) and board[row][col] == ' ':
                        board[row][col] = 'X'
                        break
                    else:
                        print("Invalid input. Please enter again.")
                except ValueError:
                    print("Invalid input. Please enter again.")
        
        # AI player's turn (using minimax with Alpha-Beta pruning)
        else:
            print("AI player (O) is thinking...")
            best_move = get_best_move(board)
            board[best_move[0]][best_move[1]] = 'O'

        # Check for winner or tie
        result = check_winner(board)
        if result == 'X':
            print_board(board)
            print("Player X wins!")
            break
        elif result == 'O':
            print_board(board)
            print("Player O (AI) wins!")
            break
        elif result == 'Tie':
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch turn
        turn = 'O' if turn == 'X' else 'X'

if __name__ == "__main__":
    main()
