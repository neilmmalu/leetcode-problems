# Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Input:  [1, 2, 3, 4]
# Output: [24, 12, 8, 6]

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    # Strategy:
    # Create lProd and rProd for each index
    # Multiply them
    # Space complexity is O(2n)

    # lProd = [None]*len(nums)
    # rProd = [None]*len(nums)

    # lProd[0] = 1
    # rProd[-1] = 1

    # for i in range(1, len(lProd)):
    #     lProd[i] = lProd[i-1]*nums[i-1]
    
    # for i in range(len(rProd)-2, -1, -1):
    #     rProd[i] = rProd[i+1]*nums[i+1]
    
    # return [lProd[i] * rProd[i] for i in range(len(nums))]

    res = [None]*len(nums)

    res[0] = 1

    for i in range(1, len(nums)):
        res[i] = nums[i-1]*res[i-1]

    prod = 1

    for i in range(len(nums)-1, -1, -1):
        res[i] = res[i]*prod
        prod *= nums[i]
    
    return res

if __name__ == "__main__":
    input = [1, 2, 3, 4]
    print(productExceptSelf(input))

