from sys import argv
import random

y=0
x=0
drs=[
'left',
'right',
'up',
'down'
]
dr = None

rf = open(argv[1]).readlines()
board = [list(x) for x in rf]

while True:
    if board[y][x] == '>':
        dr = 'left'
    elif board[y][x] == '<':
        dr = 'right'
    elif board[y][x] == 'v':
        dr = 'down'
    elif board[y][x] == '^':
        dr = 'up'
    elif board[y][x] == 'p':
        print(board[y+1][x],end='')
    elif board[y][x] == 'P':
        print(board[y-1][x],end='')
    elif board[y][x] == 'n':
        print()
    elif board[y][x] == '#':
        exit()

    if dr == 'left':
        x = x + 1
    elif dr == 'right':
        x = x - 1
    elif dr == 'up':
        y = y - 1
    elif dr == 'down':
        y = y + 1
