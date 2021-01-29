'''
Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Input: s = "bab", t = "aba"
Output: 1

Input: s = "leetcode", t = "practice"
Output: 5

Input: s = "anagram", t = "mangaar"
Output: 0
'''

from collections import Counter


def minSteps(s: str, t: str) -> int:
    '''
        Strategy:
        How many steps to convert t to s
        So keep count of chars in s and t
        Calculate the diff of each chars and add them up
    '''

    return sum((Counter(list(s)) - Counter(list(t))).values())
