import random

# Configuración del tablero
LADO = 10
ESPACIADO_HORIZONTAL = 3
BOMBA = "@"
MARCA = ">"
MINAS = 5

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
def imprimirPistes(matriu, mostrarMines: bool):
    if mostrarMines:
        imprimir(matriu)
    return



# Ompli la matriu demanera aleatòria amb un numero de mines indicat com argument.
def minar(matriu, minas: int) -> None:
    while minas > 0:
        randomRow = random.randint(0, 9)
        randomCol = random.randint(0, 9)
        if not matriu[randomRow][randomCol] == BOMBA:
            matriu[randomRow][randomCol] = BOMBA
            minas = minas - 1


# Retorna true si la posició passada està dins de la matriu.

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

# Marca o desmarca una casilla com a possibilitat de mina.
def marcar(matriu, fil: int, col: int):
    if matriu[fil][col] == "X":
        matriu[fil][col] = ">"
    else:
        print("Error: casella no valida")
    return


# Total mines marcades
def marcades(matriu) -> int:
    marcades = 0
    for i in matriu:
        for j in range(len(i)):
            if i[j] == ">":
                marcades = marcades + 1
    return marcades


# Despata la casella de la posició indicada. Returna si hem destapat una mina o no.
def minaAt(matriuMines, fil: int, col: int) -> bool:
    return matriuMines[fil][col] == BOMBA

def destapar(matriuJugador, matriuMines, fil: int, col: int):
    if not estaDins(matriuJugador, fil, col):
        return False
    if destapadaAt(matriuJugador, fil, col):
        return False
    if minaAt(matriuMines, fil, col):
        print("BOOM!")
        return True

    mines = contarMines(matriuMines, fil, col)
    if mines > 0:
        matriuJugador[fil][col] = str(mines)
        return False
    else:
        matriuJugador[fil][col] = "."
        for i in range(3):
            for j in range(3):
                minX = i + fil -1
                minY = j + col -1
                destapar(matriuJugador, matriuMines, minX, minY)

# Retorna si la casella està o no destapada.
def destapadaAt(matriu, fil: int, col: int) -> bool:
    return matriu[fil][col] == "."


# Retorna quantes caselles hi han destapades.
def destapades(matriu) -> int:
    destapades = 0
    for i in range(len(matriu)):
        for j in range(len(matriu[i])):
            if matriu[i][j] == "." or matriu[i][j].isdigit() :
                destapades = destapades + 1
    return destapades

def triarMarcarDestapar():
    while True:
        opcio = input("Vols destapar o marcar una casella? ( d/m ) ")
        if not (opcio.lower() == "d" or opcio.lower() == "m"):
            print("Error, torna a probar")
            continue
        return opcio

def entreZeroINou(num):
    return num <= 9 and num >= 0

def triarFilaColumna():
    fila = 0
    columna = 0
    while True:
        input_fila = input("Tria la Fila 0-9: ")
        input_columna = input("Tria la Columna 0-9: ")
        try:
            fila = int(input_fila)
            columna = int(input_columna)
            if not (entreZeroINou(fila) and entreZeroINou(columna)):
                print("Valor fuera de rango. Prueba de nuevo.")
                continue
        except:
            print("Error, no es un numero. Prueba de nuevo.")
            continue
        break

    return fila, columna

# menu de joc
def jugar(matriuJugador, matriuMines):
    while True:
        jugada = triarMarcarDestapar()
        fila, columna = triarFilaColumna()
        if jugada == "m":
            marcar(matriuJugador, fila, columna)

        if jugada == "d":
            # comprobem si hi ha mina
            if minaAt(matriuMines, fila, columna):
                matriuJugador[fila][columna] = BOMBA
                imprimir(matriuJugador)
                print("Has Perdut!!")
                return
            else:
                destapar(matriuJugador, matriuMines, fila, columna)

        imprimir(matriuJugador)
        totalMarcades = marcades(matriuJugador)
        totalDestapades = destapades(matriuJugador)
        total = totalMarcades + totalDestapades
        print("Marcades = " + str(totalMarcades) )
        print("Destapades = " + str(totalDestapades) )
        print("Total = " + str(total))

        if totalDestapades == (LADO * LADO) - MINAS:
            print("Has guanyat!!")
            return

def començarPartida():
    # Creem 2 matrius, la que veu el jugador, taulerJugador, y la que te les respostes, taulerPistes
    taulerJugador = [["X" for i in range(LADO)] for j in range(LADO)]
    taulerMines = [["X" for i in range(LADO)] for j in range(LADO)]

    # afegim les mines aleatoriament
    minar(taulerMines, MINAS)

    #imprimir(taulerMines)

    # Ensenyem tauler al jugador
    imprimir(taulerJugador)

    jugar(taulerJugador, taulerMines)

# Punt d'entrada del programa
començarPartida()
