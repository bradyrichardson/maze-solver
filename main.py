from SolverClasses.maze import Maze
from SolverClasses.moves import Moves
import random

maze = Maze(start=-1, end=-1, nodeList=[], foundation=[], currentPos=[], possibleYMoves=[], possibleXMoves=[])

maze.foundation = [  # hard-code the maze object's foundation array, walls are denoted by 0s and paths are denoted by 1s
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0]
]
maze.start = maze.findStart()
maze.end = [maze.findEnd(), len(maze.foundation) - 1]
maze.currentPos = [maze.findStart(), 0]

maze.printMaze()

currentYPos = 0  # start at top array
currentXPos = maze.start

moves = Moves(visitedPaths=[], possibleMoves=[])

moves.visitedPaths = []  # implement visited array and nodes to speed up process
moves.visitedNodes = []

while maze.currentPos != maze.end:
    print('Current Position: ', maze.currentPos)
    moves.visitedPaths.append(maze.currentPos)
    maze.currentPos = maze.findPath(currentYPos, currentXPos, moves)



    if maze.currentPos == maze.end:
        print('Current Position: ', maze.currentPos)
        print('Maze solved!')
    currentXPos = maze.currentPos[0]
    currentYPos = maze.currentPos[1]

