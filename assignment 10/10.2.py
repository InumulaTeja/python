import copy
def solve(col, row, board, n):
    # Check left row
    for i in range(col):
        if board[row][i] == "Q":
            return False
    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1
    # Check lower-left diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == "Q":
            return False
        i += 1
        j -= 1
    return True

def answer(col, board, ans, n):
    if col == n:
        # Save the board configuration
        ans.append(copy.deepcopy(board))
        return
    for row in range(n):
        if solve(col, row, board, n):
            board[row][col] = "Q"
            answer(col + 1, board, ans, n)
            board[row][col] = "."

n = int(input("Enter the value of n: "))
board = [["."] * n for _ in range(n)]
ans = []
answer(0, board, ans, n)

# Print all solutions
for solution in ans:
    for row in solution:
        print(" ".join(row))
    print()
