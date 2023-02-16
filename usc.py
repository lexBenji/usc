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
Str = ''

rf = open(argv[1]).readlines()
br = [list(x) for x in rf]

while True:
    if br[y][x] == '>':
        dr = 'left'
    elif br[y][x] == '<':
        dr = 'right'
    elif br[y][x] == 'v':
        dr = 'down'
    elif br[y][x] == '^':
        dr = 'up'
    elif br[y][x] == 'O':
        dr = random.choice(drs)
    elif br[y][x] == 'p':
        Str += br[y+1][x]
    elif br[y][x] == 'P':
        Str += br[y-1][x]
    elif br[y][x] == 'n':
        Str += '\n'
    elif br[y][x] == '#':
        break

    if dr == 'left':
        if x + 1 < 0:
            dr = None
        else:
            x = (x + 1) % len(br[y])
    elif dr == 'right':
        if x - 1 < 0:
            dr = None
        else:
            x = (x - 1) % len(br[y])
    elif dr == 'up':
        if y - 1 < 0:
            dr = None
        else:
            y = (y - 1) % len(br)
    elif dr == 'down':
        if y + 1 < 0:
            dr = None
        else:
            y = (y + 1) % len(br)
    
print(Str,end='')
