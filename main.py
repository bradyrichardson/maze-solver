from SolverClasses.maze import Maze
from SolverClasses.moves import Moves
import random

maze = Maze(start=-1, end=-1, nodeList=[], foundation=[], currentPos=[], possibleYMoves=[], possibleXMoves=[])

maze.foundation = [  # hard-code the maze object's foundation array
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0]
]
maze.start = maze.findStart()
maze.end = [maze.findEnd(), len(maze.foundation) - 1]
maze.currentPos = [0, maze.findStart()]

maze.printMaze()

currentYPos = 0  # start at top array
currentXPos = maze.start

moves = Moves(visited=False, visitedArray=[], possibleMoves=[])

moves.visitedArray = [] #implement visited array and nodes to speed up process

while maze.currentPos != maze.end:
    print('Current Position: ', maze.currentPos)
    moves.visitedArray.append(maze.currentPos)
    maze.currentPos = maze.findPath(currentYPos, currentXPos, moves)
    currentXPos = maze.currentPos[0]
    currentYPos = maze.currentPos[1]

print('Current Position: ', maze.currentPos)
print('End: ', maze.end)