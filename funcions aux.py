def nivellDificultat():
    """Rutina per a triar el nivell de dificultat durant la partida"""
    while True:
        print("Tria el nivell de dificultat: ")
        print("Apreta 1 per a principiant")
        print("Apreta 2 per a mitjà")
        print("Apreta 3 per a advançat")

        try:
            nivell = int(input())

        except:
            print("Error, valor incorrecte, proba de nou")
            continue

        if nivell < 1 or nivell > 3:
            print("Error, el valor ha de estar entre 1 i 3")
            continue

        break

    if nivell == 1:
        COSTAT = 9
        MINES = 10
    if nivell == 2:
        COSTAT = 16
        MINES = 40
    if nivell == 3:
        COSTAT = 24
        MINES = 99

