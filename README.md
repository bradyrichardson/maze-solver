# maze-solver
Algorithm I wrote to solve simple mazes that correspond to specific rules—no previous formal Python, algorithms, or data structures experience. Will eventually optimize.

##UPDATE
Finished writing the algorithm so that now, rather than aimlessly wander the maze, the computer tracks nodes at certain junctions, explores all possible pathways one at a time in a single direction, and if a dead end is reached, it backtracks to the previous node. If THAT node has no possible moves (aka the computer has previously completed the possible moves from that node) then the computer recursively backtracks until the ancestor node is reached and explores new directions

##DISCLAIMER
I have very little Python experience (or programming experience in general) and I know that the code is sloppy...going to try to fix it up and make it look pretty/run more efficiently. This was entirely written by me, but the node idea was inspired by a youtube video on Dijkstra's algorithm 
