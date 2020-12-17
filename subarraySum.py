# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

# Input: nums = [1, 1, 1], k = 2
# Output: 2

# Input: nums = [1, 2, 3], k = 3
# Output: 2

from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    # Strategy:
    # Add running sum to dict
    # If running sum - curr exists in the dict, add to count

    sums = {}
    sums[0] = 1
    total = 0
    count = 0

    for num in nums:
        total += num
        count += sums.get(total-k, 0)
        sums[total] = sums.get(total, 0) + 1
    
    return count

if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(subarraySum(nums, k))
    
