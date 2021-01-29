'''
This question is about implementing a basic elimination algorithm for Candy Crush.

Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent different types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the current board.
'''

from typing import List


def candyCrush(board: List[List[int]]) -> List[List[int]]:
    R, C = len(board), len(board[0])
    todo = False
    # Identification

    for i in range(R):
        for j in range(C - 2):
            if board[i][j] and \
                    abs(board[i][j]) == abs(board[i][j+1]) == abs(board[i][j+2]):
                board[i][j] = board[i][j+1] = board[i][j+2] = - \
                    abs(board[i][j])
                todo = True

    for i in range(R - 2):
        for j in range(C):
            if board[i][j] and \
                    abs(board[i][j]) == abs(board[i+1][j]) == abs(board[i+1][j]):
                board[i][j] = board[i+1][j] = board[i+2][j] = -abs(board[i][j])
                todo = True

    # Crush and gravity

    for j in range(C):
        bottomMostZero = R - 1

        for i in reversed(range(R)):
            if board[i][j] > 0:
                board[bottomMostZero][j] = board[i][j]
                bottomMostZero -= 1
        while bottomMostZero >= 0:
            board[bottomMostZero][j] = 0
            bottomMostZero -= 1

    return candyCrush(board) if todo else board
