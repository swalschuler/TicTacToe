from QLearn import updateQTable
from random import randint

# Manual input?
USER_INPUT = False
PC_INPUT = False

# Game history (treat as stack)
GHistory = []

board = []
def clearBoard():
    global board
    board = [[0, 0, 0] for i in range(3)]

def userTurn():

    if USER_INPUT:
        row, col = input("Format row col: ").split()
        row = int(row)
        col = int(col)
    else:
        row, col = randint(0, 2), randint(0, 2)

    if board[row][col] == 0:
        board[row][col] = 1
    else:
        userTurn()

gameOver = 0
def checkVictory():
    # No winner = 0, Player = 1, PC = 2
    global gameOver
    gameOver = 0

    # Check rows
    for row in board:
        # If player wins
        if all(list(map(lambda x: x == 1, row))):
            gameOver = 1

        # Computer wins
        if all(list(map(lambda x: x == 2, row))):
            gameOver = 2


    # Check cols
    for c in range(3):
        col = [board[r][c] for r in range(3)]
        # If player wins
        if all(list(map(lambda x: x == 1, col))):
            gameOver = 1

        # Computer wins
        if all(list(map(lambda x: x == 2, col))):
            gameOver = 2

    # Check diag
    if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        gameOver = 1

    if board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
        gameOver = 1

    if board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
        gameOver = 2

    if board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
        gameOver = 2

    # Check for cat's game
    if all(board[0] + board[1] + board[2]):
        gameOver = 3

    if gameOver == 1:
        print("Player wins")
        updateQTable(-1, GHistory)
    elif gameOver == 2:
        print("PC Wins")
        updateQTable(1, GHistory)

    if gameOver == 3:
        print("Cat's game")
        updateQTable(.5, GHistory)

def computerTurn():
    print("Computer turn")
    row, col = input("Format row col: ").split()
    row = int(row)
    col = int(col)
    if board[row][col] == 0:
        board[row][col] = 2
    else:
        computerTurn()

    GHistory.append([str(board), rowColToIndex(row,col)])

def rowColToIndex(row, col):
    return (row * 3) + col


def displayBoard():
    for row in board:
        print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))

def gameLoop():
    global gameOver

    if not gameOver:
        userTurn()
        displayBoard()
        checkVictory()
    if not gameOver:
        computerTurn()
        displayBoard()
        checkVictory()

    if not gameOver:
        gameLoop()

def startGame():
    global gameOver
    gameOver = 0
    clearBoard()
    gameLoop()


if __name__ == "__main__":
    startGame()
