def dfsIterative(startRow, startCol, seen, matrix):
    stack = []
    stack.append([startRow, startCol])

    while len(stack) > 0:
        current = stack.pop()
        row = current[0]
        col = current[1]

        if (row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or seen[row][col]):
            continue

        seen[row][col] = True
        print(matrix[row][col], " ")

        stack.append([row - 1, col])  # Up
        stack.append([row + 1, col])  # Down
        stack.append([row, col - 1])  # Left
        stack.append([row, col + 1])  # Right


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
seen = [[False, False, False] * 1 for _ in range(len(matrix))]
startRow = 0
startCol = 0


print("\nIterative DFS traversal:")
dfsIterative(startRow, startCol, seen, matrix)
