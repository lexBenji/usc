#!/usr/bin/python3

from sys import argv
import random

rf = open(argv[1]).readlines()
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

br = [list(x) for x in rf]

while True:
    if i > (len(cell) - 1):
        i = 0
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
    elif br[y][x] == '/':
        if i - 1 < 0:
            if cell[i] == cell[len(cell) - 1]:
                if dr == 'l':
                    dr = 'j'
                elif dr == 'j':
                    dr = 'h'
                elif dr == 'k':
                    dr = 'l'
                elif dr == 'h':
                    dr = 'k'
            else:
                dr = dr
        else:
            if cell[i] == cell[i - 1]:
                if dr == 'l':
                    dr = 'j'
                elif dr == 'j':
                    dr = 'h'
                elif dr == 'k':
                    dr = 'l'
                elif dr == 'h':
                    dr = 'k'
            else:
                dr = dr
    elif br[y][x] == '#' or br[y][x].upper() == 'E':
        break

    if dr == 'l':
        x = (x + 1) % len(br[y])
    elif dr == 'h':
        x = (x - 1) % len(br[y])
    elif dr == 'j':
        y = (y + 1) % len(br)
    elif dr == 'k':
        y = (y - 1) % len(br)
    
if br[y][x].lower() == 'e':
    for c in cell:
        if c == 0:
            pass
        else:
            print(chr(cell[cell.index(c)]))
else:
    for c in cell:
        if c == 0:
            pass
        else:
            print(f'{cell.index(c)}:{cell[cell.index(c)]}')
