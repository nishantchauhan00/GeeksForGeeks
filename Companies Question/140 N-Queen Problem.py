# it is similar to sudoku, only the definition of safe and some rules changes


def solver(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    out = []

    def isSafe(row, col):
        # as we are filling row by row, so no need to check in row

        # check column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # check diagonal(only upper left and right, as we have not yet
        # filled down diagonal)
        # upper left
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # upper right
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def helper(row, curr):
        if row == n:
            out.append("[" + curr + "]")
            return

        # recursion
        for col in range(n):
            if isSafe(row, col):
                board[row][col] = 1
                helper(row + 1, curr + str(col + 1) + " ")
                # if doesnt work then backtrack
                board[row][col] = 0

    helper(0, "")
    if len(out) == 0:
        print("-1 ")
    else:
        print(" ".join(out))


for _ in range(int(input())):
    n = int(input())
    solver(n)
