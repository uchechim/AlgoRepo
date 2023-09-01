# Python3 program for the above approach
from collections import deque as queue
 
# Direction vectors
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]
d = 'test2'
 
# Function to check if a cell
# is be visited or not
def isValid(vis, row, col):
   
    # If cell lies out of bounds
    if (row < 0 or col < 0 or row >= 3 or col >= 2):
        return False
 
    # If cell is already visited
    if (vis[row][col]):
        return False
 
    # Otherwise
    return True
 
# Function to perform the BFS traversal
def BFS(grid, vis, row, col):
   
    # Stores indices of the matrix cells
    q = queue()
 
    # Mark the starting cell as visited
    # and push it into the queue
    q.append(( row, col ))
    vis[row][col] = True
 
    # Iterate while the queue
    # is not empty
    while (len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        print(grid[x][y], end = " ")
 
        # Go to the adjacent cells
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(vis, adjx, adjy)):
                q.append((adjx, adjy))
                vis[adjx][adjy] = True
 

   
# Given input matrix
grid= [ [ 1, 3],
        [ 2, 3],
        [ 3, 1],
        ]

# Declare the visited array
vis = [[ False, False] for i in range(len(grid))]
# vis, False, sizeof vis)

BFS(grid, vis, 0, 0)

# This code is contributed by mohit kumar 29.