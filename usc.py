#!/usr/bin/python3

from sys import argv
import random
from board import board

y=0
x=0
drs = [
        'l',
        'h',
        'j',
        'k'
        ]
dr = None
cell = [0,0,0,0,0,0,0,0]
i = 0

br = [list(x) for x in board]

while True:
    if cell[i] < 0:
        cell[i] = 0
    if br[y][x] == '>':
        i = i + 1
        dr = 'l'
    elif br[y][x] == '<':
        i = i - 1
        dr = 'h'
    elif br[y][x] == 'v':
        cell[i] = cell[i] - 1
        dr = 'j'
    elif br[y][x] == '^':
        cell[i] = cell[i] + 1
        dr = 'k'
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
    
for c in cell:
    if c == 0:
        pass
    else:
        print(f'{c}: {cell[c]}')
