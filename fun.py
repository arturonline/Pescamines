fil = 4
col = 4
side = 4

m = [["1", "2", "3", "4"], ["a", 5,"b", "c"], ["q","w","e", "r"], ["j","k","l", 5]]

for i in m:
    print(i)

def foraTauler(matriu, fil, col):
    side = len(m)
    return fil < 0 or col < 0 or fil >= side or col >= side


def contarMines(matriu, fil, col):
    count = 0
    for i in range(3):
        for j in range(3):
            minX = i + fil -1
            minY = j + col -1
            if foraTauler(matriu, minX, minY):
                print(f"OOB => matriu[{minX}][{minY}]")
            else:
                print(f"matriu[{minX}][{minY}] = {matriu[minX][minY]}")
                if matriu[minX][minY] == 5:
                    count = count + 1
    return count

print(contarMines(m, 3, 3))

