from .moves import Moves
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

    def findStart(self):
        for i, col in enumerate(self.foundation[0]):
            if col == 1:
                return i

    def findEnd(self):
        for i, col in enumerate(self.foundation[len(self.foundation) - 1]):
            if col == 1:
                return i

    def printMaze(self):
        for row in self.foundation:
            print(row)

    # could make this algorithm faster if I just searched adjacent spaces
    def findPath(self, currentY, currentX, moveObj):

        self.idPossibleMoves(currentY, currentX, moveObj)

        if len(moveObj.possibleMoves) > 1:  # if there is more than one possible move, the current position is a node
            self.nodeList.append(self.currentPos)

        # print('Possible moves: ', moveObj.possibleMoves) #make a move
        return self.makeMove(moveObj, currentY, currentX)

    # going to make random decision
    def makeMove(self, moveObj, currentY, currentX):
        newPos = []

        # insert some sort of node function that checks the last node and then goes back if needed
        if len(moveObj.possibleMoves) == 0 and self.currentPos != self.end: # check if dead end has been reached
            newPos = moveObj.goToNode(self, currentY, currentX)
            return newPos

        if len(moveObj.possibleMoves) != 0:
            newPos = moveObj.possibleMoves[random.randint(0, len(moveObj.possibleMoves) - 1)]
            moveObj.possibleMoves.clear()
            return newPos


# still need to add function that counts num moves possible, so that you can go 2+ nodes back if needed

    def idPossibleMoves(self, currentY, currentX, moveObj):
        # clear the arrays that store possible single-coordinate moves
        if len(moveObj.possibleMoves) > 0:
            moveObj.possibleMoves.clear()
        if len(self.possibleYMoves) > 0:
            self.possibleYMoves.clear()
        if len(self.possibleXMoves) > 0:
            self.possibleXMoves.clear()

        # iterate through upper array (unless on top)
        if currentY != 0:
            for i, canMove in enumerate(self.foundation[currentY - 1]):
                if canMove == 1 and abs(currentX - i) == 0 and [currentX, currentY]:
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