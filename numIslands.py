# Given an m x n 2d grid map of '1's(land) and '0's(water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# Input: grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]
# Output: 1

# Input: grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]
# Output: 3

import queue
from typing import List

def numIslands(grid: List[List[str]]) -> int:
    # Strategy:
    # Do BFS on first "1". Every time a "1" is visited, set it to "0" to mark it as visited.
    # Count the number of times BFS is carried out => number of islands
    numIslands = 0
    numRows, numCols = len(grid), len(grid[0])

    for i in range(numRows):
        for j in range(numCols):
            #New land encountered
            if grid[i][j] == "1":
                #Add land to final count
                numIslands += 1
                #Mark unit as visited
                grid[i][j] = "0"
                neighbors = queue.Queue()
                #Add coords to queue
                neighbors.put((i, j))
                while not neighbors.empty():
                    #Pop from queue
                    row, col = neighbors.get()

                    #Add adjacent land neighbors to queue
                    #Mark them as visited (because they're part of the same island)
                    if row + 1 < numRows and grid[row+1][col] == "1":
                        neighbors.put((row+1, col))
                        grid[row+1][col] = "0"
                    if row - 1 >= 0 and grid[row-1][col] == "1":
                        neighbors.put((row-1, col))
                        grid[row-1][col] = "0"
                    if col + 1 < numCols and grid[row][col+1] == "1":
                        neighbors.put((row, col+1))
                        grid[row][col+1] = "0"
                    if col - 1 >= 0 and grid[row][col-1] == "1":
                        neighbors.put((row, col-1))
                        grid[row][col-1] = "0"
                

    return numIslands


if __name__ == "__main__":
    grid = [
            ["1", "0", "1", "1", "1"],
            ["1", "0", "1", "0", "1"], 
            ["1", "1", "1", "0", "1"]
        ]

    print(numIslands(grid))

    
