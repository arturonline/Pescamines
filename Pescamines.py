import random
from colorama import Fore, Back, Style

# Configuració del tauler
COSTAT = 10
ESPACIADO_HORIZONTAL = 4
BOMBA = '⨶'
MARCA = '▶'
MINES = 5
TITOL = " Ρescamines "

# Funcions per a dibuixar el tauler de joc

def mostrarTitol():
    """Dibuixa la linia de la capçalera amb el nom del joc"""
    print()
    print(Style.BRIGHT + TITOL.center(ESPACIADO_HORIZONTAL * COSTAT + 7, 'Ξ') + Style.RESET_ALL)
    print()

def printLiniaNumeros():
    """Dibuixa una linia de números"""
    numeros = [i for i in range(COSTAT)]
    fila = " " * 5
    for i in numeros:
        fila = fila + str(i).ljust(ESPACIADO_HORIZONTAL, " ")
    print(Fore.BLUE + fila + Style.RESET_ALL)

def printLlimitSuperior():
    """Dibuixa la primera linia de simbols que conformen les caselles"""
    sostre_inici = "╔═"
    sostre_mitja = "══╦═"
    sostre_final = "══╗"
    for i in range(COSTAT):
        fila = "   " + sostre_inici + sostre_mitja * (COSTAT -1) + sostre_final
    print(fila)

def printLlimitInferior():
    """Dibuixa la ultima linia de simbols que conformen les caselles"""
    sol_inici = "╚═"
    sol_mitja = "══╩═"
    sol_final = "══╝"
    for i in range(COSTAT):
        fila = "   " + sol_inici + sol_mitja * (COSTAT -1) + sol_final
    print(fila)

def printLiniaIntermitja():
    """Dibuixa la linia intermitja de simbols que conformen les caselles"""
    mitja_inici = "╠═"
    mitja_mitja = "══╬═"
    mitja_final = "══╣"
    for i in range(COSTAT):
        fila = "   " + mitja_inici + mitja_mitja * (COSTAT -1) + mitja_final
    print(fila)

def printLinia(matriu):
    """Dibuixa el contingut de la matriu en les caselles i el separa"""
    fila = ""
    for row in range(len(matriu)):
        fila = Fore.RED + str(row) + Style.RESET_ALL + "  ║ "
        for col in range(len(matriu[row])):
            fila = fila + matriu[row][col] + " ║ "

        print(fila + " " + Fore.RED + str(row) + Style.RESET_ALL)
        if row != len(matriu) - 1:
            printLiniaIntermitja()

def imprimir(matrix):
    """Imprimix una matriu pasada con parametre"""
    mostrarTitol()
    printLiniaNumeros()
    printLlimitSuperior()
    printLinia(matrix)
    printLlimitInferior()
    printLiniaNumeros()
    print()

# Funcions per a fer comprobacions

def minar(matriu, mines: int) -> None:
    """Ompli la matriu demanera aleatòria amb un numero de mines indicat com argument."""
    while mines > 0:
        randomRow = random.randint(0, COSTAT -1)
        randomCol = random.randint(0, COSTAT -1)
        if not matriu[randomRow][randomCol] == BOMBA:
            matriu[randomRow][randomCol] = BOMBA
            mines = mines - 1



def estaDins(matriu, fil: int, col: int) -> bool:
    """Retorna true si la posició passada està dins de la matriu."""
    side = len(matriu)
    return fil >= 0 and col >= 0 and fil < side and col < side


def contarMines(matriu, fil: int, col: int) -> int:
    """Conta el número de mines alrededor de una posició passada com argument."""
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

def marcar(matriu, fil: int, col: int):
    """Marca o desmarca una casilla com a possibilitat de mina."""
    if matriu[fil][col] == "X":
        matriu[fil][col] = Fore.GREEN + ">" + Style.RESET_ALL
    else:
        print("Error: casella no valida")
    return


def marcades(matriu) -> int:
    """Retorna el total de mines marcades."""
    marcades = 0
    for i in matriu:
        for j in range(len(i)):
            if i[j] == ">":
                marcades = marcades + 1
    return marcades


def minaAt(matriuMines, fil: int, col: int) -> bool:
    """Retorna si hem destapat una mina a la posició passada."""
    return matriuMines[fil][col] == BOMBA

def destapar(matriuJugador, matriuMines, fil: int, col: int):
    """Despata la casella de la posició indicada."""
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

def destapadaAt(matriu, fil: int, col: int) -> bool:
    """Retorna si la casella està destapadada a la posició passada."""
    return matriu[fil][col] == "."


def destapades(matriu) -> int:
    """Retorna quantes caselles hi han destapades."""
    destapades = 0
    for i in range(len(matriu)):
        for j in range(len(matriu[i])):
            if matriu[i][j] == "." or matriu[i][j].isdigit() :
                destapades = destapades + 1
    return destapades

def triarMarcarDestapar():
    """Durant la partida presenta al usuari la opció de destapar o marcar"""
    while True:
        opcio = input("  ▶ Vols destapar o marcar una casella? ( d/m ) ")
        if not (opcio.lower() == "d" or opcio.lower() == "m"):
            print("Error, torna a probar")
            continue
        return opcio

def entreZeroINou(num)-> bool:
    """Retorna si un número esta entre 0 i 9 ambdos inclosos"""
    return num <= 9 and num >= 0

# Funcions per a inicialitzar el joc i els menus

def triarFilaColumna():
    """Durant la partida presenta al usuari la opció per triar fila o columna"""
    fila = 0
    columna = 0
    while True:
        input_fila = input(Fore.RED + "  ↪ Tria la Fila 0-9: " + Style.RESET_ALL)
        input_columna = input(Fore.BLUE + "  ↪ Tria la Columna 0-9: " + Style.RESET_ALL)
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

def jugar(matriuJugador, matriuMines):
    """Presenta els menus de joc per al usuari i fa seguiment i control de la partida."""
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
        print("  ■ Marcades".ljust((COSTAT + 1) * 4, '.') + str(totalMarcades) )
        print("  ■ Destapades".ljust((COSTAT + 1) * 4, '.') + str(totalDestapades) )
        print("  ■ Total".ljust((COSTAT + 1) * 4,'.') + str(total))
        print()
        if totalDestapades == (COSTAT * COSTAT) - MINES:
            print(Fore.MAGENTA + "Has guanyat!!".center(50) )
            print("Final de Partida".center(50) + Style.RESET_ALL)
            print()
            return

def Començar():
    """Punt d'entrada del programa. Initialitza les matrius i llança les rutines per a començar a jugar"""
    # Creem 2 matrius, la que veu el jugador, taulerJugador, y la que te les mines, taulerMines
    taulerJugador = [["X" for i in range(COSTAT)] for j in range(COSTAT)]
    taulerMines = [["X" for i in range(COSTAT)] for j in range(COSTAT)]

    # afegim les mines aleatoriament
    minar(taulerMines, MINES)

    # Ensenyem tauler al jugador
    imprimir(taulerJugador)

    jugar(taulerJugador, taulerMines)

Començar()