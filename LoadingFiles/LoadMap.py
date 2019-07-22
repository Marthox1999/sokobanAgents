import sys


def searchMap():

    boxes = []
    map = []
    for line in sys.stdin:
        stripped = line.strip()
        if not stripped:
            break
        map.append(stripped)
    
    try:
        map.remove('\n')
    except:
        0

    for i in range (0, len(map)):
        map[i]= map[i].replace('\n', '')

    witdh, height = len(map[0]), 0

    for i in range(0, len(map)):
        if(("W" in map[i]) or ("0" in map[i])):
            height = height+1

    playerPosition = map[height].split(',')

    for i in range(height+1, len(map)):
        boxes.append(map[i].split(','))

    for i in range (len(map)):
        print(map[i])

    for i in range (len(boxes)):
        for j in range (len(boxes[i])):
            try:
                boxes[i][j] = int(boxes[i][j])
            except ValueError:
                return -1

    for i in range (len(playerPosition)):
        try:
            playerPosition[i] = int(playerPosition[i])
        except ValueError:
            return -1

    return map, playerPosition, boxes
