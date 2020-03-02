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
    while numero > 0:
        randomRow = random.randint(0, 9)
        randomCol = random.randint(0, 9)
        if matriu[randomRow][randomCol] == BOMBA:
            continue
        matriu[randomRow][randomCol] = BOMBA
        numero = numero - 1


# Retorna true si la posició passada està dins de la matriu.
def foraMatriu(matriu, fil, col):
    side = len(matriu)
    return fil < 0 or col < 0 or fil >= side or col >= side


def contarMines(matriu, fil, col):
    count = 0
    for i in range(3):
        for j in range(3):
            minX = i + fil -1
            minY = j + col -1
            if foraMatriu(matriu, minX, minY):
                print(f"OOB => matriu[{minX}][{minY}]")
            else:
                if matriu[minX][minY] == BOMBA:
                    count = count + 1
    return count


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
    for i in matriu:
        for j in range(len(i)):
            if i[j] == ">":
                marcades = marcades + 1
    return marcades

def contarMines(matriu, fil, col):
    count = 0
    i= fil -1
    j= col -1
    for i in range(3):
        for j in range(3):
            if matriu[i][j] == BOMBA:
                count = count + 1
    return count

# Despata la casella de la posició indicada. Returna si hem destapat una mina o no.
def destapar(matriu, fil, col):


    # cas base


    # Comprobem que no estiga destapada:

    if destapadaAt(matriu, fil, col):
        return False
    # comprobem si hi ha mina
    if minaAt(matriu, fil, col):
        matriu[fil][col] = BOMBA
        imprimir(matriu)
        print("Has Perdut!!")
        return True

    else:
    # Loop over all surrounding cells
        count = 0
        minx= fil -1
        miny= col -1
        for i in range(3):
            for j in range(3):
                count = count + 1
        if count > 0:
            matriu[fil][col] = count
        else:
            destapar(matriu, )




# Retorna si la casella està o no destapada.
def destapadaAt(matriu, fil, col):
    return matriu[fil][col] == " "



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
