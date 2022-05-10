print()
print('Welcome to Tic Tac Toe!')
currentPlayer = input("Choose between X or O. ")
winner: None
gameRunning = True
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

def main():
    while gameRunning:
        createBoard(board)
        playerInput(board)
        checkWin()
        checkDraw(board)
        switchPlayer()
        if gameRunning != False:
            printTurn(currentPlayer)
    print("Good game. Thanks for playing!")

def createBoard(board):
    """Create Tic Tac Toe Board"""
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board):
    """Take player input"""
    user_input = int(input("Enter a number 1-9: "))
    if user_input >= 1 and user_input <= 9 and board[user_input-1] == "-":
        board[user_input-1] = currentPlayer
    else:
        print("Player is already in that spot!")

# check for WIN or DRAW
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkDraw(board):
    global gameRunning
    if "-" not in board:
        createBoard(board)
        print("The game is a DRAW!")
        gameRunning = False

def checkWin():
    global gameRunning 
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        print(f"The WINNER is {winner}.")
        gameRunning = False

# Switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Print current player
def printTurn(currentPlayer):
    if gameRunning == False:
        exit()
    else:
        print(f"It's {currentPlayer}'s turn to choose a square.")

# Call main to start this program.
if __name__ == "__main__":
    main()
