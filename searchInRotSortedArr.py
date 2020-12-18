# You are given an integer array nums sorted in ascending order, and an integer target.

# Suppose that nums is rotated at some pivot unknown to you beforehand(i.e., [0, 1, 2, 4, 5, 6, 7] might become[4, 5, 6, 7, 0, 1, 2]).

# If target is found in the array return its index, otherwise, return -1.

# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
# Output: 4

# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
# Output: -1

# Input: nums = [1], target = 0
# Output: -1

from typing import List

def search(nums: List[int], target: int) -> int:
    # Strategy: check element at midpoint
    # If max of right is less than mid, inflection point is on right
    # If min of left is more than mid, inflection point is on the left

    if not nums:
        return 0
    N = len(nums)

    i, j = 0, N-1

    while i <= j:
        mid = (i + j)//2
        if nums[mid] == target:
            return mid
        if nums[i] > nums[mid]:
            #Inflection point is on the left
            if target < nums[i] and target > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        elif nums[j] < nums[mid]:
            #Inflection point is on the right
            if target > nums[j] and target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1
        else:
            if target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1
    return -1

if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1]
    target = 9
    print(search(nums, target))
