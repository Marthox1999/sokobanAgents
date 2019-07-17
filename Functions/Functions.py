

def playerPositionToInt(playerPosition):
    for i in range len(playerPosition):
        try:
            playerPosition[i] = int(playerPosition[i])
        except ValueError:
            return -1
    print(playerPosition)
    return 1

def boxesPositionsToInt(boxesPositions):
    for i in range (len(boxes)):
        for j in range (len(boxes[i])):
            try:
                boxesPositions[i][j] = int(boxesPositions[i][j])
            except ValueError:
                return -1
    print(boxesPositions)
    return 1
