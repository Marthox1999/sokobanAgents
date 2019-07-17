
def searchMap():
    global fileName
    print("\n Seleccione el nivel de zokoban")
    print("para los niveles locales ingrese 'Levels/%nivel%'")

    fileName = input("ingrese el path: ")
    print(fileName)
    boxes = []
    sokobanMap = open(fileName,"r")
    map = sokobanMap.readlines()
    map.remove('\n')

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

    print("player position", playerPosition)
    print("boxes in map", boxes)

    return map, playerPosition, boxes
