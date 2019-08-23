from SolverClasses.maze import Maze
from SolverClasses.moves import Moves


maze = Maze(start=-1, end=-1, nodeList=[], foundation=[], currentPos=[], possibleYMoves=[], possibleXMoves=[])

maze.foundation = [  # hard-code the maze object's foundation array, walls are denoted by 0s and paths are denoted by 1s
    [0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
maze.findEnds()
# maze.findEnd()
maze.currentPos = maze.start
maze.printMaze()
print('s: ', maze.start)
print('e: ', maze.end)

currentXPos = maze.start[0]
currentYPos = maze.start[1]

moves = Moves(visitedPaths=[], possibleMoves=[])

moves.visitedPaths = []
moves.visitedNodes = []

while maze.currentPos != maze.end:
    print('Current Position: ', maze.currentPos)

    moves.visitedPaths.append(maze.currentPos)  # append position to the visitedPaths array to prevent moving backwards

    maze.currentPos = maze.findPath(currentYPos, currentXPos, moves)  # find the next move

    if maze.currentPos == maze.end:  # when you have reached the end, print the position and celebrate
        print('Current Position: ', maze.currentPos)
        print('Maze solved!')

    currentXPos = maze.currentPos[0]  # assign passed-in x and y values after a new current position is found
    currentYPos = maze.currentPos[1]

