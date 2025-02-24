def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    
    pass

board = [[" " for _ in range(3)] for _ in range(3)]
print_board(board)
