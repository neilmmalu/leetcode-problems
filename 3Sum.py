# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]

# Input: nums = []
# Output: []

# Input: nums = [0]
# Output: []

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    # -4 -1 -1 0 1 2
    if len(nums) < 3:
        return []
    
    nums = sorted(nums)
    result = set()

    for i in range(len(nums)):
        target = -nums[i]
        comps = {}
        for j in range(i+1, len(nums)):
            comp = target - nums[j]
            if comp in comps:
                result.add((nums[i], comp, nums[j]))   
            else:
                comps[nums[j]] = comp
    return list(result)

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))
