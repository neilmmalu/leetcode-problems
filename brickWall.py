# There is a brick wall in front of you.The wall is rectangular and has several rows of bricks.The bricks have the same height but different width.You want to draw a vertical line from the top to the bottom and cross the least bricks.

#  The brick wall is represented by a list of rows.Each row is a list of integers representing the width of each brick in this row from left to right.

#   If your line go through the edge of a brick,
#    then the brick is not considered as crossed.You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

#      You cannot draw a line just along one of the two vertical edges of the wall,
#     in which case the line will obviously cross no bricks.

# Input: [[1, 2, 2, 1 ],
#          [3, 1, 2],
#          [1, 3, 2],
#          [2, 4],
#          [3, 1, 2],
#          [1, 3, 1, 1] ]

#       Output: 2

from typing import List


def leastBricks(wall: List[List[int]]) -> int:
    '''
        Strategy:
        1 3 5 6
        3 4 6
        1 4 6
        2 6
        3 4 6
        1 4 5 6
    '''

    if not wall:
        return 0

    breakCount = {}

    maxWidth = sum(wall[0])

    for row in wall:
        width = 0
        for brick in row:
            width += brick
            if width < maxWidth:
                if width in breakCount:
                    breakCount[width] += 1
                else:
                    breakCount[width] = 1

    return (len(wall) - max(breakCount.values())) if breakCount else len(wall)


if __name__ == "__main__":
    wall = [[1, 2, 2, 1],
            [3, 1, 2],
            [1, 3, 2],
            [2, 4],
            [3, 1, 2],
            [1, 3, 1, 1]]
    print(leastBricks(wall))
