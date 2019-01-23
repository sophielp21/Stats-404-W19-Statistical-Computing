import random

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '
            }
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turnoptions = {'X', "O"}
turn = random.sample(turnoptions,1)

def get_empty_positions(board):
    try:
        return [key for (key,value) in board.items() if value == ' ']
    except TypeError:
        print(f"Tie")

def winner(board, move):
    return ((board['top-L'] == move and board['top-M'] == move and board['top-R'] == move) or # top across
        (board['mid-L'] == move and board['mid-M'] == move and board['mid-R'] == move) or # middle across
        (board['low-L'] == move and board['low-M'] == move and board['low-R'] == move) or # bottom across
        (board['top-L'] == move and board['mid-L'] == move and board['low-L'] == move) or # left down 
        (board['top-M'] == move and board['mid-M'] == move and board['low-M'] == move) or # middle down
        (board['top-R'] == move and board['mid-R'] == move and board['low-R'] == move) or # right down 
        (board['top-L'] == move and board['mid-M'] == move and board['low-R'] == move) or # left diagonal
        (board['top-R'] == move and board['mid-M'] == move and board['low-M'] == move)) # right diagonal

for i in range(9):
    move = str(random.sample(get_empty_positions(theBoard),1))
    cleanmove = move[2:7]
    theBoard[cleanmove] = turn
    if winner(theBoard, turn):
        print(f"{turn} is Winner")
        break
        if turn == ['X']:
            turn = ['O']
        else:
            turn = ['X']