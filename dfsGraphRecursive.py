def dfsRecursive(row, col, seen, matrix):
    
    #Edge case -> Out of bounds or Previously Visited Node
    if (
        row < 0
        or col < 0
        or row >= len(matrix)
        or col >= len(matrix[0])
        or seen[row][col] == True
    ):
        return

    #Mark the current node/element as visited to avoid cycles.
    seen[row][col] = True

    print(matrix[row][col], " ")

    #Explore each unvisited neighbor of the current node/element recursively by calling the DFS function with the neighbor as the new current position
    #Backtrack if all neighbors have been visited or if there are no unvisited neighbors.

    dfsRecursive(row - 1, col, seen, matrix)  # Up

    dfsRecursive(row + 1, col, seen, matrix)  # Down

    dfsRecursive(row, col - 1, seen, matrix)  # Left

    dfsRecursive(row, col + 1, seen, matrix)  # Right
    


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""
[1, 2, 3]
[4, 5, 6] 
[7, 8, 9]]
"""
seen = [[False] * 3 for _ in range(3)]


print("Recursive DFS traversal:")
#Choose a starting node or element as the current position.
dfsRecursive(0, 0, seen, matrix)






