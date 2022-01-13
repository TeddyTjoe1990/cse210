import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(f"{Fore.RED}>Tic-Tac-Toe<")
print(f"{Fore.RED} By Teddy")
print()
def main():
    pl = upc_pl("")
    board = play_board()
    while not (win(board) or tie(board)):
        game_board(board)
        movement(pl, board)
        pl = upc_pl(pl)
    game_board(board)
    print(f"{Fore.BLUE}Good game. Thanks for playing!")
    print()

def play_board():
    board = []
    for answer in range(9):
        board.append(answer + 1)
    return board
    
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

def movement(pl, board):
    answer = int(input(f"{pl}'s turn to choose a square (1-9): "))
    board[answer - 1] = pl

def upc_pl(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

def game_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")

if __name__ == "__main__":
    main()