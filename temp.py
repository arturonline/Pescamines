# Configuració del tauler
COSTAT = 10
ESPACIADO_HORIZONTAL = 4
BOMBA = "@"
MARCA = ">"
MINES = 5
Tauler = "═ ║ ╔ ╦ ╗ ╠ ╬ ╣ ╚ ╩ ╝"

# print('  A   B   C   D   E   F   G   H   I')
# print('╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')
# print('╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
# print('╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝')

matriu = [["X" for i in range(COSTAT)] for j in range(COSTAT)]

def mostrarTitol():
    print()
    print(' Pescamines '.center(ESPACIADO_HORIZONTAL * COSTAT + 7, '='))
    print()

def printLiniaNumeros():
    """Dibuixa una linia de números"""
    numeros = [i for i in range(COSTAT)]
    fila = " " * 5
    for i in numeros:
        fila = fila + str(i).ljust(ESPACIADO_HORIZONTAL, " ")
    print(fila)

def printLlimitSuperior():
    fila = ""
    sostre_inici = "╔═"
    sostre_mitja = "══╦═"
    sostre_final = "══╗"
    for i in range(COSTAT):
        fila = "   " + sostre_inici + sostre_mitja * (COSTAT -1) + sostre_final
    print(fila)

def printLlimitInferior():
    fila = ""
    sol_inici = "╚═"
    sol_mitja = "══╩═"
    sol_final = "══╝"
    for i in range(COSTAT):
        fila = "   " + sol_inici + sol_mitja * (COSTAT -1) + sol_final
    print(fila)

def printLiniaIntermitja():
    fila = ""
    mitja_inici = "╠═"
    mitja_mitja = "══╬═"
    mitja_final = "══╣"
    for i in range(COSTAT):
        fila = "   " + mitja_inici + mitja_mitja * (COSTAT -1) + mitja_final
    print(fila)

def printLinia(matriu):
    fila = ""
    for row in range(len(matriu)):
        fila = str(row) + "  ║ "
        for col in range(len(matriu[row])):
            fila = fila + matriu[row][col] + " ║ "

        print(fila + " " + str(row))
        if row != len(matriu) - 1:
            printLiniaIntermitja()

def imprimir(matrix):
    mostrarTitol()
    printLiniaNumeros()
    printLlimitSuperior()
    printLinia(matrix)
    printLlimitInferior()
    printLiniaNumeros()
    print()
