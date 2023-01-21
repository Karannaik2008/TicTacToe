# import main
def checkWin(board):
    
    # left diagonal
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]

    # right diagonal
    elif board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    # horizontal wins
    for rows in range(3):
        if board[rows][0] == board[rows][1] == board[rows][2] != 0:
            return board[(rows)][0]

    # vertical wins
    for cols in range(3):
        if board[0][cols] == board[1][cols] == board[2][cols] != 0:
            return board[0][(cols)]

    return 0

def whosChance(p1 ,p2,chance):
    if chance%2 ==0:
        return p1
    elif chance%2 != 0:
        return p2

# def is_empty_sqr(board,rows,col):
#     board[rows][col] == 0
    
    return 1
def get_empty_sqrs(board):
    empty_sqrs=[]
    # rows,col = board
    for col in range(3):
        for rows  in range(3):
            # if board 
            if board[rows][col] == 0:
                empty_sqrs.append((rows,col))
            else:pass
    return empty_sqrs


def is_full(board):
    a = get_empty_sqrs(board)
    if len(a)>0:
        return False
    elif len(a) == 0:
        return True

def mark_sqr(board,row,col,player):
    board[row][col] = player

    # for rows in range(3):
    #     for cols in range(3):
    #         if 
