print(">Tic-Tac-Toe<")

def main():
    player = next_player("")
    board = play_board()
    while not (win(board) or tie(board)):
        game_board(board)
        movement(player, board)
        player = next_player(player)
    game_board(board)
    print("Good game. Thanks for playing!") 

def play_board():
    board = []
    for answer in range(9):
        board.append(answer + 1)
    return board

def game_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    
def tie(board):
    for answer in range(9):
        if board[answer] != "x" and board[answer] != "o":
            return False
    return True 
    
def win(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def movement(player, board):
    answer = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[answer - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()