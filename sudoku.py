def get_user_input():
    print("Enter your Sudoku puzzle row by row (use 0 for empty spaces):")
    board = []
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").strip().split()))
                if len(row) == 9 and all(0 <= num <= 9 for num in row):
                    board.append(row)
                    break
                else:
                    print("Invalid input! Please enter exactly 9 numbers between 0-9.")
            except ValueError:
                print("Invalid input! Please enter numbers only.")
    return board
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True
def print_board(board):
    for i in range(9):
        print(" ".join(str(num) for num in board[i]))
        if i % 3 == 2 and i != 8:
            print("-" * 21)
sudoku_board = get_user_input()
print("\nOriginal Sudoku Puzzle:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku:")
    print_board(sudoku_board)
else:
    print("\nNo solution exists.")