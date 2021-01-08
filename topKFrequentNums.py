# Given a non-empty array of integers, return the k most frequent elements.

# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]

# Input: nums = [1], k = 1
# Output: [1]

from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    '''
        Strategy:
        Intuition: Max frequency is n
        So create dict of all freqs
        Keep adding all nums to corr freqs
        Merge all and return last k

        O(n)
    '''

    freqs = [[] for i in range(len(nums))]

    freqD = {}

    for num in nums:
        if num in freqD:
            freqD[num] += 1
        else:
            freqD[num] = 1

    for key, value in freqD.items():
        freqs[value].append(key)

    mergedFreq = sum(freqs, [])

    return mergedFreq[::-1][:k]


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(topKFrequent(nums, k))
