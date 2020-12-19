# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate(i, ai). n vertical lines are drawn such that the two endpoints of the line i is at(i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

# Notice that you may not slant the container.

# Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49
# Explanation: The above vertical lines are represented by array[1, 8, 6, 2, 5, 4, 8, 3, 7]. In this case, the max area of water(blue section) the container can contain is 49.

from typing import List

def maxArea(height: List[int]) -> int:
    if not height:
        return 0
    
    maxArea = 0

    i, j = 0, len(height) - 1

    while i < j:
        width = j - i
        minHeight = min(height[i], height[j])
        maxArea = max(maxArea, width * minHeight)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    
    return maxArea

if __name__ == "__main__":
    height = [1, 2, 1]
    print(maxArea(height))
