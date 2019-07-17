class Node:
    def __init__(self, playerPosition, boxesPositions, father, decision):
        self.playerPosition = playerPosition
        self.boxesPositions = boxesPositions
        self.father = father
        self.decision = decision
    def moveLeft(self, map):
        leftPosition = self.playerPosition
        leftPosition[1] = leftPosition[1] - 1
        if map[leftPosition].lower() == 'w':
            return False
        return True
    def moveRight(self, map):
        rightPosition = self.playerPosition
        rightPosition[1] = rightPosition[1] + 1
        if map[rightPosition].lower() == 'w':
            return False
        return True
    def moveUp(self, map):
        upPosition = self.playerPosition
        upPosition[0] = upPosition[0] - 1
        if map[upPosition].lower() == 'w':
            return False
        return True
    def moveDown(self, map):
        downPosition = self.playerPosition
        downPosition[0] = downPosition[0] +1
        if map[downPosition].lower() == 'w':
            return False
        return True
    def victory(self, map):
        for box in boxesPositions:
            if map[box] == 'x':
                return True
            return False
