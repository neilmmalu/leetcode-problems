'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
'''
from collections import Counter


def isAnagram(self, s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    countS = Counter(s)
    countT = Counter(t)

    for k, v in countS.items():
        if countT[k] != v:
            return False

    return True
