from SolverClasses.maze import Maze
from SolverClasses.moves import Moves
import random

maze = Maze(start=-1, end=-1, nodeList=[], foundation=[], currentPos=[], possibleYMoves=[], possibleXMoves=[])

maze.foundation = [  # hard-code the maze object's foundation array, walls are denoted by 0s and paths are denoted by 1s
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 0, 0, 1, 0],  # it is assumed that the top array and the bottom array hold the start and end, respectively, this can be changed
    [0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
]

maze.findStart()
print(maze.start)
maze.findEnd()
print(maze.end)
maze.currentPos = maze.start
maze.printMaze()

currentXPos = maze.start[0]
currentYPos = maze.start[1]

moves = Moves(visitedPaths=[], possibleMoves=[])

moves.visitedPaths = []  # implement visited array and nodes to speed up process
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

