
"""
Recur for all 8 adjacent cells

        N.W   N   N.E
            \   |   /
                \  |  /
        W----Cell----E
                / | \
            /   |  \
        S.W    S   S.E

Cell-->Current Cell (row, col)
N -->  North        (row-1, col)
S -->  South        (row+1, col)
E -->  East         (row, col+1)
W -->  West            (row, col-1)
N.E--> North-East   (row-1, col+1)
N.W--> North-West   (row-1, col-1)
S.E--> South-East   (row+1, col+1)
S.W--> South-West   (row+1, col-1)
"""


import random

# Configuración del tablero
LADO = 10
ESPACIADO_HORIZONTAL = 3
BOMBA = "@"
MARCA = ">"

# Funcions

# mostra capçalera
def printLiniaNumeros():
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # primera fila en numeros
    fila1 = " " * 3
    for i in numeros:
        fila1 = fila1 + str(i).ljust(ESPACIADO_HORIZONTAL, " ")
    print(fila1)

# Mostra per pantalla una matriu. Esposarà tant dalt, baix,a dreta i a esquerre el numero de fila.
def imprimir(matriu):
    # titol
    print()
    print('Pescamines'.center(ESPACIADO_HORIZONTAL * LADO + 4, '-'))
    print()

    printLiniaNumeros()
    fila = ""
    for row in range(len(matriu)):
        fila = str(row) + " " * 2
        for col in range(len(matriu[row])):
            fila = fila + matriu[row][col].ljust(ESPACIADO_HORIZONTAL, " ")
        print(fila + str(row))
    printLiniaNumeros()
    print()


# Mostra el tauler de les pistes. Depenent del booleà es mostraran o no les mines.
def imprimirPistes(matriu, mostrarMines):
    if mostrarMines:
        imprimir(matriu)
    return



# Ompli la matriu demanera aleatòria amb un numero de mines indicat com argument.
def minar(matriu, numero):
    for i in range(numero):
        randomRow = random.randint(0, 9)
        randomCol = random.randint(0, 9)
        if matriu[randomRow][randomCol] == BOMBA:
            i = i - 1  # para los resultados que se repiten
        matriu[randomRow][randomCol] = BOMBA



# Retorna true si la posició passada està dins de la matriu.
def dinsMatriu(matriu, fil, col):
    return (fil < 0 or fil > LADO) and (col < 0 or col > LADO)


# Retorna true si hi ha una mina a la posició que es passa com argument.
def minaAt(matriu, fil, col):
    return matriu[fil][col] == BOMBA



# Marca o desmarca una casilla com a possibilitat de mina.
def marcar(matriu, fil, col):
    matriu[fil][col] = MARCA
    return


# Total mines marcades
def marcades(matriu):
    marcades = 0
    for i in range(len(matriu)):
        for j in range(len(matriu[i])):
            if matriu[i][j] == ">":
                marcades = marcades + 1
    return marcades



# Despata la casella de la posició indicada.Returna si hem destapat una mina o no.
def destapar(matriu, fil, col):
    # cas base
    if matriu[fil][col] != 'X':
        return False

    # comprobem si hi ha mina
    if minaAt(matriu, fil, col):
        matriu[fil][co] = BOMBA
        imprimir(matriu)
        print("Has Perdut!!")
        return True

    # Loop over all surrounding cells
    if dinsMatriu(matriu, fil, col):
        minx= fil -1
        miny= col -1
        for minx in range(fil + 2):
            for miny in range(col + 2):
                return
    


# Retorna si la casella està o no destapada.
def destapadaAt(matriu, fil, col):
    return not (matriu[fil][col] == "X" or matriu[fil][col] == BOMBA or matriu[fil][col] == MARCA)



# Retorna quantes caselles hi han destapades.
def destapades(matriu):
    destapades = 0
    for i in range(len(matriu)):
        for j in range(len(matriu[i])):
            if destapadaAt(matriu, i, j):
                destapades = destapades + 1
    return destapades


# menu de joc
def mostrarMenu(matriu):
    # opcio = input("Vols destapar o marcar una casella? ( d/m ) ")
    # while True:
    #     opcio = input("Vols destapar o marcar una casella? ( d/m ) ")
    #     if not (opcio.lower() == "d" or opcio.lower() == "m"):
    #         print("Error, torna a probar")
    #         continue
    #     break
    # Aqui marquem casella o desmarquem casella
    while True:
        try:
            fila = int(input("Trial la Fila 0-9: "))
            columna  = int(input("Tria la Columna 0-9: "))
        except:
            print("Error, torna a probar")
        break
    print("Marcades =  " + str(marcades(matriu)))
    print("Destapades = " + str(destapades(matriu)))
    print("Total = ")

def començarPartida():
    # Creem 2 matrius, la que veu el jugador, taulerJugador, y la que te les respostes, taulerPistes
    taulerJugador = [["X" for i in range(LADO)] for j in range(LADO)]
    taulerPistes = [["X" for i in range(LADO)] for j in range(LADO)]

    # afegim les mines aleatoriament
    minar(taulerPistes, 25)

    gameOver = False
    while gameOver:
        imprimir(taulerJugador)
        mostrarMenu(taulerJugador)

# Punt d'entrada del programa
començarPartida()
