class Moves:
    def __init__(self, visitedPaths, possibleMoves):
        self.visitedPaths = []
        self.possibleMoves = []

    def checkIfVisited(self, possibleMove):  # check if it has already been visited,
        for prevMove in self.visitedPaths:   # if so, do not append it into possible moves
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

        mazeObj.idPossibleMoves(currentY, currentX, self)  # find possible moves at the revisited node

        if len(self.possibleMoves) == 0:                     # if no moves are available at that previous node,
            mazeObj.nodeList.pop(len(mazeObj.nodeList) - 1)  # recursively move to the next previous node and
                                                             # remove earlier previous node from the node list
            self.goToNode(mazeObj, currentY, currentX)

            if len(self.possibleMoves) > 0:  # recursive return will come back here before exiting the function
                return mazeObj.currentPos
        else:
            return newPos