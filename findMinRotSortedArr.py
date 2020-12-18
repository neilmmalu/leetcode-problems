# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0, 1, 2, 4, 5, 6, 7] might become:

# [4, 5, 6, 7, 0, 1, 2] if it was rotated 4 times.
# [0, 1, 2, 4, 5, 6, 7] if it was rotated 7 times.
# Notice that rotating an array[a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array[a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums, return the minimum element of this array.

# Input: nums = [3, 4, 5, 1, 2]
# Output: 1
# Explanation: The original array was[1, 2, 3, 4, 5] rotated 3 times.

# Input: nums = [4, 5, 6, 7, 0, 1, 2]
# Output: 0
# Explanation: The original array was[0, 1, 2, 4, 5, 6, 7] and it was rotated 4 times.

# Input: nums = [11, 13, 15, 17]
# Output: 11
# Explanation: The original array was[11, 13, 15, 17] and it was rotated 4 times.

from typing import List

def findMin(nums: List[int]) -> int:
    # Strategy: check element at midpoint
    # If max of right is less than mid, inflection point is on right
    # If min of left is more than mid, inflection point is on the left
    if not nums:
        return 0
    N = len(nums)

    if N == 1:
        return nums[0]
    
    i, j = 0, N-1

    while i < j:
        mid = (i + j)//2
        if mid != 0 and nums[mid-1] > nums[mid]:
            return nums[mid]
        if nums[i] > nums[mid]:
            j = mid - 1
        elif nums[j] < nums[mid]:
            i = mid + 1
        else:
            return nums[i]
    return nums[i]

if __name__ == "__main__":
    nums = [2, 1]
    print(findMin(nums))
