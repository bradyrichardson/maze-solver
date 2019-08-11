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
            moveObj.possibleMoves.append(addMove)

        # potentially parse indices instead of using another array
        # print('Possible moves: ', moveObj.possibleMoves)
        return self.makeMove(moveObj)

    # going to make random decision to get to end
    def makeMove(self, moveObj):
        newPos = []
        if len(moveObj.possibleMoves) != 0:
            newPos = moveObj.possibleMoves[random.randint(0, len(moveObj.possibleMoves) - 1)]
        return newPos
