'''
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
'''

from collections import Counter


def firstUniqChar(s: str) -> int:
    counts = Counter(list(s))

    return s.index([k for k, v in counts.items() if v == 1][0])


if __name__ == "__main__":
    print(firstUniqChar("abcdfabcde"))
