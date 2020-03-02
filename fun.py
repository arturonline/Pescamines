m = [[1,2,3], [4,5,6], [7,8,9]]

for i in m:
    print(i)

def printM(m):
    for i in range(3):
        for j in range(3):
            print(m[i][j])

for i in range(3):
    for j in range(3):
        if m[i][j] == 5:
            m[i][j] = 0

print()


for i in m:
    print(i)
