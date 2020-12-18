# Given an integer array nums, find the contiguous subarray(containing at least one number) which has the largest sum and return its sum.

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.

# Input: nums = [1]
# Output: 1

from typing import List

def maxSubArray(nums: List[int]) -> int:
    # Strategy:
    # Calculate running sum. If running sum is negative, move left and right
    # Otherwise move right
    # -2 1 -2 4 3 5 6 1 5

    N = len(nums)

    if N == 1:
        return nums[0]
    
    sums = []

    i = 0
    runningSum = 0

    while i < N:
        runningSum += nums[i]
        sums.append(runningSum)
        if runningSum < 0:
            runningSum = 0
        
        i += 1
        
    return max(sums)

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))

