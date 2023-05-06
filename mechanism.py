from random import randint, sample
from secrets import choice

def printOut(peta):
    for i in peta:
        for j in i:
            print(j, end = " ")
        print() 

def cekTitik(i, j, peta):
    sekitar = []
    for n in range(-1, 2):
        for m in range(-1,2):
            if i + n < 0 or i + n > N - 1:
                continue
            if j + m < 0 or j + m > N - 1:
                continue
            if peta[i+n][j+m] == "*":
                continue
            sekitar.append([i + n, j + m])

    return sekitar

def cekSekitar(i, j, k, l, peta):
    for n in range(-1, 2):
        for m in range(-1,2):
            if i + n < 0 or i + n > N - 1:
                continue
            if j + m < 0 or j + m > N - 1:
                continue
            if j + m == l and i + n == k:
                continue
            if peta[i+n][j+m] == "*":
                return False

    return True
        
def mapAlgorithm(peta, routePoint):
    # peta[0][0] = "*"
    i, j = sample(range(0, N-1), 2)
    sekitar = cekTitik(i, j, peta)
    while len(sekitar) != 0:
        next_titik = []
        for k in sekitar:
            if cekSekitar(k[0], k[1], i, j, peta):
                next_titik.append(k)
        if len(next_titik) == 0:
            break
        acak = sample(next_titik, 1) 
        i = acak[0][0]
        j = acak[0][1]
        peta[i][j] = "*"
        routePoint.append([i, j])
        sekitar = cekTitik(i, j, peta)
    peta[routePoint[0][0]][routePoint[0][1]] = "S"
    peta[i][j] = "X"

def makeMap(routePoint, peta, challengePoint):
    peta = [[" " for i in range(N)] for i in range(N)]
    while len(routePoint) < 3*N:
        routePoint = []
        peta = [[" " for i in range(N)] for i in range(N)]
        mapAlgorithm(peta, routePoint)
    challengePoint = makeChallenge(peta, routePoint, challengePoint)
    peta = makeBackground(peta)
    return peta, routePoint, challengePoint

def makeChallenge(peta, routePoint, challengePoint):
    temp = len(routePoint)//3
    challengePoint = sample(range(3, len(routePoint) - 4), temp)
    for i in challengePoint:
        peta[routePoint[i][0]][routePoint[i][1]] = "!"
    return challengePoint

def makeBackground(peta):
    # simbol = [".", ",", "@", "#", "$", " ", "-", "%", ">", "<", "?", "+"]
    simbol = [" ", " ", " ", " "," ", " ", " ", "+", "?"]
    for i in range(len(peta)):
        for j in range(len(peta[0])):
            if peta[i][j] == " ":
                peta[i][j] = choice(simbol)
    
    return peta

def updateMap(coordinate, peta, playerPosition, challengePoint, routePoint):
    if coordinate == 0:
        peta[routePoint[coordinate][0]][routePoint[coordinate][1]] = "S"
    elif coordinate in playerPosition:
        peta[routePoint[coordinate][0]][routePoint[coordinate][1]] = playerPosition.index(coordinate) + 1
    elif coordinate in challengePoint:
        peta[routePoint[coordinate][0]][routePoint[coordinate][1]] = "!"
    else:
        peta[routePoint[coordinate][0]][routePoint[coordinate][1]] = "*"
    
    return peta

def diceRoll(playerNum, peta, playerPosition, routePoint, challengePoint):
    global dice
    dice = randint(1, 6)
    # print(f"Player {playerNum+1} dapat angka", dice)
    playerPosition[playerNum] += dice
    if playerPosition[playerNum] > len(routePoint) - 1:
        peta = updateMap(playerPosition[playerNum] - dice, peta, playerPosition, challengePoint, routePoint)
        playerPosition[playerNum] = 2*(len(routePoint) - 1) - playerPosition[playerNum]
    peta[routePoint[playerPosition[playerNum]][0]][routePoint[playerPosition[playerNum]][1]] = playerNum + 1
    return peta, playerPosition, dice
    
def changePlayer(P, playerPosition):
    playerPosition = [0 for i in range(P)]
    return playerPosition

N = 20 






