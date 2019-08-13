class Moves:
    def __init__(self, visitedPaths, possibleMoves):
        self.visitedPaths = []
        self.possibleMoves = []

    def checkIfVisited(self, possibleMove): # check if it has already been visited, if so, do not append it into possible moves
        for prevMove in self.visitedPaths:
            if possibleMove == prevMove:
                return True
        return False

    def goToNode(self, mazeObj, currentY, currentX):
        print('Returning to previous node...')
        mazeObj.currentPos = mazeObj.nodeList[len(mazeObj.nodeList) - 1]
        newPos = []
        newPos = mazeObj.currentPos
        currentX = mazeObj.currentPos[0]
        currentY = mazeObj.currentPos[1]
        mazeObj.idPossibleMoves(currentY, currentX, self)

        if len(self.possibleMoves) == 0:
            # pop back node
            mazeObj.nodeList.pop(len(mazeObj.nodeList) - 1)
            self.goToNode(mazeObj, currentY, currentX)
            if len(self.possibleMoves) > 0:
                return mazeObj.currentPos
        else:
            return newPos