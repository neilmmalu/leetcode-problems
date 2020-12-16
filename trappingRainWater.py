# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
# Explanation: The above elevation map(black section) is represented by array[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]. In this case, 6 units of rain water(blue section) are being trapped.

from typing import List

def trap(height: List[int]) -> int:
    if not height:
        return 0
    rMax = [None]*len(height)
    lMax = [None]*len(height)
    lMax[0] = height[0]
    rMax[-1] = height[-1]
    for i in range(1,len(height)):
        lMax[i] = max(height[i], lMax[i-1])
    
    for i in range(len(height)-2, -1, -1):
        rMax[i] = max(height[i], rMax[i+1])
    
    ans = 0
    for i in range(len(height)):
        ans += min(lMax[i], rMax[i]) - height[i]

    return ans

if __name__ == "__main__":
    height = [4, 2, 0, 3, 2, 5]
    print(trap(height))
