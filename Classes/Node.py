import copy

class Node:
    def __init__(self, playerPosition, boxesPositions, father, decision):
        self.playerPosition = playerPosition
        self.boxesPositions = boxesPositions
        self.father = father
        self.decision = decision

    def expandNode(self, map):
        playerPosition = copy.deepcopy(self.playerPosition)
        boxesPositions = copy.deepcopy(self.boxesPositions)

        moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        posibleStates = []

        for move in moves:
            newBoxesPositions = boxesPositions[:]
            newPosition = [playerPosition[0] + move[0], playerPosition[1] + move[1]]

            if map[newPosition[0]][newPosition[1]].lower() == 'w':
                continue

            for index, box in enumerate(boxesPositions):
                if newPosition == box:
                    newBoxPosition = [box[0] + move[0], box[1] + move[1]]
                    if map[newBoxPosition[0]][newBoxPosition[1]].lower() == 'w':
                        continue
                    if newBoxPosition in boxesPositions:
                        continue
                    newBoxesPositions[index] = newBoxPosition

            print("newPosition:", newPosition, " newBoxPosition:", newBoxesPositions)
            newMoveNode = Node(newPosition, newBoxesPositions, self, move)
            posibleStates.append(newMoveNode)

        return posibleStates

    def findPath(self):
        path = []
        fatherNode = self.father
        while fatherNode != None:
            path.append(fatherNode.decision)
            fatherNode = fatherNode.father
        return path

    def findCicle(self):
        fatherNote = self.father
        while (fatherNode != None and
                fatherNode.playerPosition != self.playerPosition and
                fatherNode.boxesPositions != self.boxesPositions):
                fatherNode = fatherNode.father

    def victory(self, map):
        for box in self.boxesPositions:
            if map[box] == 'x':
                return True
            return False
