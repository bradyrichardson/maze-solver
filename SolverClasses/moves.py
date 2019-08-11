class Moves:
    def __init__(self, visited, visitedArray, possibleMoves):
        self.visited = False
        self.visitedArray = []
        self.possibleMoves = []

    def checkCanMove(self):
        for moves in self.possibleMoves:
            print(moves)