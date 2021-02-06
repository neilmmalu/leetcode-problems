'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
'''

from typing import List
from collections import deque


def wordBreak(s: str, wordDict: List[str]) -> bool:
    '''
        Strategy:
        BFS solution using startswith. 
        If string starts with word, substring it, add word to q, visited and repeat

        DP:
        dp = [True] + [False]*len(s)
        for word in wordDict:
            for i in range(1, len(s) + 1):
                if s[:i].endswith(word):
                    dp[i] |= dp[i-len(word)]
        return dp[-1]
    '''

    q = deque()
    q.append(s)
    seen = set()

    while q:
        curr = q.popleft()

        for word in wordDict:
            if curr.startswith(word):
                newString = curr[len(word):]
                if newString == "":
                    return True
                if newString not in seen:
                    seen.add(newString)
                    q.append(newString)
    return False
