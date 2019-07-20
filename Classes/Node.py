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

            newMoveNode = Node(newPosition, newBoxesPositions, self, move)
            if (newMoveNode.findCicle()):
                continue
            else:
                posibleStates.append(newMoveNode)
        return posibleStates

    def findPath(self):
        moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        path = []
        movePath = []
        actual = self
        while (actual.father != None):
            path.append(actual.decision)
            actual = actual.father
        for decision in reversed(path):
            if(decision==[-1, 0]):
                move="Up"
            if(decision==[0, 1]):
                move="Right"
            if(decision==[1, 0]):
                move="Down"
            if(decision==[0, -1]):
                move="Left"
            movePath.append(move)
        return movePath

    def findCicle(self):
        actual = self
        fatherNode = self.father
        while (fatherNode != None):
            if(fatherNode.playerPosition == actual.playerPosition and
                fatherNode.boxesPositions == actual.boxesPositions):
                return True
            else:
                fatherNode = fatherNode.father
        return False

    def victory(self, map):
        for box in self.boxesPositions:
            if map[box[0]][box[1]].lower() == 'x':
                return True
            return False
