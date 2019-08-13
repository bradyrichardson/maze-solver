import random


class Maze:
    def __init__(self, start, end, nodeList, foundation, currentPos, possibleYMoves, possibleXMoves):
        self.start = []
        self.end = []
        self.nodeList = []
        self.foundation = []
        self.currentPos = []
        self.possibleYMoves = []
        self.possibleXMoves = []

    def findStart(self):  # finds the starting point
        for i, col in enumerate(self.foundation[0]):
            if col == 1:
                self.start = [i, 0]
        for i, col in enumerate(self.foundation):
            if self.foundation[i][0] == 1:
                self.start = [0, i]

    def findEnd(self):  # finds an int that represents the end point FIXME make so it also checks the last column
        for i, col in enumerate(self.foundation[len(self.foundation) - 1]):
            if col == 1:
                self.end = [i, len(self.foundation) - 1]
        for i, col in enumerate(self.foundation):
            if self.foundation[i][len(self.foundation[i]) - 1] == 1:
                self.end = [len(self.foundation[i]) - 1, i] # fix this to make the end right, otherwise errors get thrown]

    def printMaze(self):
        for row in self.foundation:
            print(row)

    # FIXME could make this algorithm faster if I just searched adjacent spaces
    def findPath(self, currentY, currentX, moveObj):

        self.idPossibleMoves(currentY, currentX, moveObj)

        if len(moveObj.possibleMoves) > 1:  # if there is more than one possible move, the current position is a node
            self.nodeList.append(self.currentPos)

        return self.makeMove(moveObj, currentY, currentX)  # make a move based on the list of possible moves

    def makeMove(self, moveObj, currentY, currentX):
        newPos = []

        if len(moveObj.possibleMoves) == 0 and self.currentPos != self.end:  # check if dead end has been reached
            newPos = moveObj.goToNode(self, currentY, currentX)
            return newPos

        if len(moveObj.possibleMoves) != 0:
            newPos = moveObj.possibleMoves[random.randint(0, len(moveObj.possibleMoves) - 1)]
            moveObj.possibleMoves.clear()
            return newPos

    def idPossibleMoves(self, currentY, currentX, moveObj):
        # clear the arrays that store possible moves
        if len(moveObj.possibleMoves) > 0:
            moveObj.possibleMoves.clear()
        if len(self.possibleYMoves) > 0:
            self.possibleYMoves.clear()
        if len(self.possibleXMoves) > 0:
            self.possibleXMoves.clear()

        # iterate through upper array (unless on top)
        if currentY != 0:
            for i, canMove in enumerate(self.foundation[currentY - 1]):
                if canMove == 1 and abs(currentX - i) == 0:
                    self.possibleYMoves.append(currentY - 1)
                    self.possibleXMoves.append(i)

        # iterate through current array
        for i, canMove in enumerate(self.foundation[currentY]):
            if canMove == 1 and currentX != i and abs(currentX - i) == 1:
                self.possibleYMoves.append(currentY)
                self.possibleXMoves.append(i)

        # iterate through lower array (unless on bottom)
        if currentY != len(self.foundation) - 1:
            for i, canMove in enumerate(self.foundation[currentY + 1]):
                if canMove == 1 and abs(currentX - i) == 0:
                    self.possibleYMoves.append(currentY + 1)
                    self.possibleXMoves.append(i)

        # combine possible x and y moves into single array that holds coordinates
        for i in range(len(self.possibleXMoves)):
            addMove = [self.possibleXMoves[i], self.possibleYMoves[i]]
            if moveObj.checkIfVisited(addMove) == False:  # check for and remove previous paths as possible moves
                moveObj.possibleMoves.append(addMove)