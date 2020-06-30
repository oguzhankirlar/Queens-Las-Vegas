import random

def printBoard(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print("\n")
    print("\n")

def QueensLasVegas(n):
    board = [[0 for j in range(n)] for i in range(n)]
    availColumns = []
    for a in range(n):
        availColumns.append(a)
    R = 0
    while len(availColumns) != 0 and R < n:
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
    printBoard(board, n)
    return 1

def isSafe(board, row, col):
    for i in range(col):
        if board[row][i]:
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

i = 0
for a in range(1000):
    if QueensLasVegas(8) == 1:
        i += 1
print(i)
print("Success rate is: ", i/1000)


