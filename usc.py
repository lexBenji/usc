#!/usr/bin/python3

from sys import argv
import random
from board import board

y=0
x=0
Str = ''
drs = [
        'l',
        'h',
        'j',
        'k'
        ]
dr = None

br = [list(x) for x in board]

while True:
    if br[y][x] == '>':
        dr = 'l'
    elif br[y][x] == '<':
        dr = 'h'
    elif br[y][x] == 'v':
        dr = 'j'
    elif br[y][x] == '^':
        dr = 'k'
    elif br[y][x].lower() == 'r':
        dr = random.choice(drs)
    elif br[y][x] == 'p':
        Str += br[y+1][x]
    elif br[y][x] == 'P':
        Str += br[y-1][x]
    elif br[y][x].lower() == 'n':
        Str += '\n'
    elif br[y][x] == '#':
        break

    if dr == 'l':
        x = (x + 1) % len(br[y])
    elif dr == 'h':
        x = (x - 1) % len(br[y])
    elif dr == 'j':
        y = (y + 1) % len(br)
    elif dr == 'k':
        y = (y - 1) % len(br)
    
print(Str,end='')
