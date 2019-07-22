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

        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        corners = [
                    [[-1, 0], [0, 1]],
                    [[1, 0], [0, 1]],
                    [[-1, 0], [0, -1]],
                    [[1, 0], [0, -1]]
                    ]
        posibleStates = []

        #Verify the posible moves and states and only return the posible states
        for move in moves:
            canMove = True
            newBoxesPositions = boxesPositions[:]
            newPosition = [playerPosition[0] + move[0], playerPosition[1] + move[1]]

            if map[newPosition[0]][newPosition[1]].lower() == 'w':
                continue

            for index, box in enumerate(boxesPositions):
                if newPosition == box:
                    newBoxPosition = [box[0] + move[0], box[1] + move[1]]
                    if map[newBoxPosition[0]][newBoxPosition[1]].lower() == 'w':
                        canMove = False
                        continue
                    if newBoxPosition in newBoxesPositions:
                        canMove = False
                        continue
                    #Check if the box will be stucked in a corner and, if that corner isnt a global
                    #didnt expand the node
                    if map[newPosition[0]][newPosition[1]].lower() != 'x':
                        for corner in corners:
                            cornerBox_1 = [newBoxPosition[0] + corner[0][0], newBoxPosition[1] + corner[0][1]]
                            cornerBox_2 = [newBoxPosition[0] + corner[1][0], newBoxPosition[1] + corner[1][1]]
                            if map[cornerBox_1[0]][cornerBox_1[1]].lower() == 'w' and map[cornerBox_2[0]][cornerBox_2[1]].lower() == 'w':
                                canMove = False
                                continue
                    del newBoxesPositions[index]
                    newBoxesPositions.insert(index, newBoxPosition)

            newMoveNode = Node(newPosition, newBoxesPositions, self, move)

            if (newMoveNode.findCicle()):
                continue
            if(canMove == False):
                continue
            else:
                posibleStates.append(newMoveNode)

        return posibleStates

    def findPath(self, map):
        moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        path = []
        movePath = []
        actual = self
        while (actual.father != None):
            path.append(actual.decision)
            actual = actual.father
        for decision in reversed(path):
            if decision == [-1,0]:
                movePath.append('U')
            if decision == [0, 1]:
                movePath.append('R')
            if decision == [1, 0]:
                movePath.append('D')
            if decision == [0, -1]:
                movePath.append('L')
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

    def findDepth(self):
        depth = 0
        fatherNode = self.father
        while (fatherNode != None):
            depth = depth + 1
            fatherNode = fatherNode.father
        return depth

    def victory(self, map):
        for box in self.boxesPositions:
            if map[box[0]][box[1]].lower() != 'x':
                return False
        return True
