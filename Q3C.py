import random
def printBoard(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print("\n")
    print("\n")

def countQueen(board, n):
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                count += 1
    return count

def isSafe(board, row, col):
    for i in range(row):
        if board[i][col]:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while i >= 0 and j < 8:
        if board[i][j]:
            return False
        i = i - 1
        j = j + 1
    return True

def solveNQueen(board, row, n):
    if row >= n:
        return True
    for j in range(n):
        if board[row][j] == 1:
            solveNQueen(board, row+1, n)
    for i in range(n):
        if isSafe(board, row, i):
            board[row][i] = 1
            if solveNQueen(board, row+1, n):
                return True
            board[row][i] = 0
    return False

def QueensLasVegas(board, n, k):
    availColumns = []
    for a in range(n):
        availColumns.append(a)
    R = 0
    while len(availColumns) != 0 and R < k:
        temp = []
        for i in availColumns:
            if isSafe(board, R, i):
                temp.append(i)
        if len(temp) == 0:
            return False
        rand = random.choice(temp)
        board[R][rand] = 1
        R += 1
        availColumns.remove(rand)
    return board

count = 0
for i in range(1000):
    board = [[0 for j in range(8)] for i in range(8)]
    b = QueensLasVegas(board, 8, 1)  # You can try to different number of queens from random with changing last parameter here
    if b is False:
        break
    solveNQueen(b, 0, 8)
    if countQueen(b, 8) == 8:
        printBoard(b, 8)
    else:
        count += 1
        print("impossible")
print(count)

