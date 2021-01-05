# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

# Input: arr = [5, 5, 4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.

# Input: arr = [4, 3, 1, 1, 3, 3, 2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

from typing import List


def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:
    if not arr:
        return 0

    counts = {}

    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    counts = dict(sorted(counts.items(), key=lambda tup: tup[1]))

    key = next(iter(counts))

    while k > 0:
        if counts[key] <= k:
            k -= counts[key]
            counts.pop(key)
            key = next(iter(counts)) if counts else None
        else:
            break

    return len(counts.keys())


if __name__ == "__main__":
    arr = [4, 3, 1, 1, 3, 3, 2]
    k = 3
    print(findLeastNumOfUniqueInts(arr, k))
