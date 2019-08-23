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

    def findEnds(self):  # finds the starting and ending points
        # iterate through top array
        for i, col in enumerate(self.foundation[0]):
            if col == 1 and len(self.start) == 0:
                self.start = [i, 0]
                continue
            if col == 1 and len(self.start) > 0:
                self.end = [i, 0]

        # iterate through bottom array
        for i, col in enumerate(self.foundation[len(self.foundation) - 1]):
            if col == 1 and len(self.start) == 0:
                self.start = [i, len(self.foundation) - 1]
                continue
            if col == 1 and len(self.start) > 0:
                self.end = [i, len(self.foundation) - 1]

        # iterate through left column
        for i, rowStart in enumerate(self.foundation):
            if rowStart[0] == 1 and len(self.start) == 0:
                self.start = [0, i]
            if rowStart[0] == 1 and len(self.start) > 0:
                self.end = [0, i]
        # iterate through right column
        for i, rowEnd in enumerate(self.foundation):
            if rowEnd[len(rowEnd) - 1] == 1 and len(self.start) == 0:
                self.start = [len(rowEnd) - 1, i]
            if rowEnd[len(rowEnd) - 1] == 1 and len(self.start) > 0:
                self.end = [len(rowEnd) - 1, i]

    def printMaze(self):
        for row in self.foundation:
            print(row)

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

        # possible upper moves
        if currentY != 0 and self.foundation[currentY - 1][currentX] == 1:
            self.possibleXMoves.append(currentX)
            self.possibleYMoves.append(currentY - 1)


        # possible left moves
        if currentX != 0:
            if self.foundation[currentY][currentX - 1] == 1:
                self.possibleXMoves.append(currentX - 1)
                self.possibleYMoves.append(currentY)

        # possible right moves
        if currentX != len(self.foundation[currentY]) - 1:
            if self.foundation[currentY][currentX + 1] == 1:
                self.possibleXMoves.append(currentX + 1)
                self.possibleYMoves.append(currentY)

        # possible lower moves
        if currentY != len(self.foundation) - 1 and self.foundation[currentY + 1][currentX] == 1:
            self.possibleXMoves.append(currentX)
            self.possibleYMoves.append(currentY + 1)

        # combine possible x and y moves into single array that holds coordinates
        for i in range(len(self.possibleXMoves)):
            addMove = [self.possibleXMoves[i], self.possibleYMoves[i]]
            if moveObj.checkIfVisited(addMove) == False:  # check for and remove previous paths as possible moves
                moveObj.possibleMoves.append(addMove)

            # **BLOCK COMMENTS ARE OLD METHOD**

            # iterate through upper array (unless on top)
            #if currentY != 0:
            #    for i, canMove in enumerate(self.foundation[currentY - 1]):
            #        if canMove == 1 and abs(currentX - i) == 0:
            #            self.possibleYMoves.append(currentY - 1)
            #            self.possibleXMoves.append(i)


            #for i, canMove in enumerate(self.foundation[currentY]):
            #    if canMove == 1 and currentX != i and abs(currentX - i) == 1:
            #        self.possibleYMoves.append(currentY)
            #        self.possibleXMoves.append(i)


            # iterate through lower array (unless on bottom)
            #if currentY != len(self.foundation) - 1:
            #    for i, canMove in enumerate(self.foundation[currentY + 1]):
            #        if canMove == 1 and abs(currentX - i) == 0:
            #            self.possibleYMoves.append(currentY + 1)
            #            self.possibleXMoves.append(i)