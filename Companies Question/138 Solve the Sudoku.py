import math

# backtracking
def solver(board):
    def isSafe(row, col, val):  # checks if it is safe to put 'val' in the box
        # check row and column
        for i in range(9):
            if board[row][i] == val or board[i][col] == val:
                return False

        # check that box
        box_x, box_y = math.floor(row / 3) * 3, math.floor(col / 3) * 3
        # print(row, col, box_x, box_y)
        for i in range(3):
            for j in range(3):
                if board[box_x + i][box_y + j] == val:
                    return False
        
        return True


    # it will return true if sudoku is solvalble otherwise false
    def sudokuSolver(row, col):
        # if reached next to last row then sudoku is solved
        if row == 9:
            return True

        # if at the end of row, i.e, at last column, then go next row
        if col == 9:
            return sudokuSolver(row + 1, 0)

        # if its already filled
        if board[row][col] != 0:
            return sudokuSolver(row, col + 1)

        # try each value at the box if safe
        for i in range(1, 10):  # as values possible are (1, 2, 3 ...9)
            if isSafe(row, col, i):
                board[row][col] = i
                # recursion
                works = sudokuSolver(row, col + 1)
                if works:
                    return True
                # if doesnt work then backtrack
                board[row][col] = 0

        return False


    if sudokuSolver(0, 0):
        return board
    else:
        return None




for _ in range(int(input())):
    n = 9
    lis = list(map(int, input().split()))
    board = []
    for i in range(0, n * n, n):
        board.append(lis[i : i + n])
    print(" ".join(" ".join(str(el) for el in row) for row in solver(board)))

