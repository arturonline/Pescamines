import random

BOMBA = "@"

def estaDins(matriu, fil: int, col: int) -> bool:
    side = len(matriu)
    return fil >= 0 and col >= 0 and fil < side and col < side


def contarMines(matriu, fil: int, col: int) -> int:
    count = 0
    for i in range(3):
        for j in range(3):
            minX = i + fil -1
            minY = j + col -1
            if minX == fil and minY == col:
                    continue
            if estaDins(matriu, minX, minY) and minaAt(matriu, minX, minY):
                count = count + 1
    return count

m = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '@', 'X'],
    ['X', 'X', 'X', 'X', '@', '@', '@', 'X', 'X', 'X'],
    ['@', '@', 'X', '@', 'X', '@', '@', 'X', 'X', 'X'],
    ['@', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['@', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', '@', 'X', 'X', 'X', 'X', '@'],
    ['X', 'X', 'X', 'X', 'X', 'X', '@', 'X', 'X', 'X'],
    ['X', 'X', '@', 'X', 'X', '@', 'X', 'X', 'X', 'X'],
    ['X', 'X', '@', 'X', 'X', '@', '@', 'X', 'X', 'X'],
    ['X', 'X', '@', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]

def destapadaAt(matriu, fil: int, col: int) -> bool:
    return matriu[fil][col] == " "

# Retorna true si hi ha una mina a la posició que es passa com argument.
def minaAt(matriu, fil: int, col: int) -> bool:
    return matriu[fil][col] == BOMBA

def destapar(matriu, fil: int, col: int):
    if not estaDins(matriu, fil, col):
        return False
    if destapadaAt(matriu, fil, col): 
        return False
    if minaAt(matriu, fil, col):
        print("BOOM!")
        return True

    mines = contarMines(matriu, fil, col)
    if mines > 0:
        matriu[fil][col] = str(mines)
        return False
    else:
        matriu[fil][col] = " "
        for i in range(3):
            for j in range(3):
                minX = i + fil -1
                minY = j + col -1
                destapar(matriu, minX, minY)

destapar(m, 0, 0)

for i in m:
    print(i)