# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Input: [1, 2, 3, 1]
# Output: true

# Input: [1, 2, 3, 4]
# Output: false

# Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: true

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    # Strategy:
    # Add to set. Compare length of set and list

    return not len(nums) == len(set(nums))

    

if __name__ == "__main__":
    input = [1, 2, 3, 1]
    print(containsDuplicate(input))
