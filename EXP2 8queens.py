def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check this column on the left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    return True

def solve_n_queens(board, col, n):
    # If all queens are placed
    if col >= n:
        return True
    
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 'Q'
            
            # Recursively place rest of the queens
            if solve_n_queens(board, col + 1, n):
                return True
            
            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = '.'
    
    # If the queen cannot be placed in any row in this column col, then return False
    return False

def solve():
    n = 8
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    if solve_n_queens(board, 0, n):
        print_board(board)
    else:
        print("No solution exists")

if __name__ == "__main__":
    solve()
