
# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell
# the value 1 representing a fresh orange
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent(4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

# Input: [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# Output: 4

# Input: [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
# Output: -1
# Explanation:  The orange in the bottom left corner(row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
from typing import List
from queue import deque

def rottingOranges(grid: List[List[int]]) -> int:
    # Strategy:
    # For all cells that have "2", add them to queue.
    # Count number of fresh oranges
    # Once 1-level BFS is done for "2" cell, increment main counter
    # If fresh orange is encountered in BFS, reduce count by 1
    # At the end check if fresh oranges = 0 and return main counter
    # Else return -1
    q = deque()
    numRows, numCols = len(grid), len(grid[0])
    freshOranges = 0
    numMinutes = -1

    for i in range(numRows):
        for j in range(numCols):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                freshOranges += 1
    
    #Add dummy to signify end of one level of BFS
    q.append((-1, -1))
    while q:
        row, col = q.popleft()
        if row == -1:
            numMinutes += 1
            #If q still has more elements, add another dummy to signify end of level
            if q:
                q.append((-1, -1))
        else:
            if row + 1 < numRows and grid[row+1][col] == 1:
                grid[row+1][col] = 2
                q.append((row+1, col))
                freshOranges -= 1
            if row - 1 >= 0 and grid[row-1][col] == 1:
                grid[row-1][col] = 2
                q.append((row-1, col))
                freshOranges -= 1
            if col + 1 < numCols and grid[row][col+1] == 1:
                grid[row][col+1] = 2
                q.append((row, col+1))
                freshOranges -= 1
            if col - 1 >= 0 and grid[row][col-1] == 1:
                grid[row][col-1] = 2
                q.append((row, col-1))
                freshOranges -= 1

    return numMinutes if freshOranges == 0 else -1

if __name__ == "__main__":
    input = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(rottingOranges(input))

