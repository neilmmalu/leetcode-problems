# A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

# Input: S = "ababcbacadefegdehijhklij"
# Output: [9, 7, 8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

from typing import List

def partitionLabels(S: str) -> List[int]:
    # For each char in string last index to a dict
    # Then iterating over each char, use a sliding window
    # windowStart = first idx of 'a' windowEnd is last idx of 'a'
    # if first idx of 'b' > windowStart and last idx of 'b' < windowStart => window unchanged
    # if first idx of 'b' > windowStart and last idx of 'b' after windowEmd then shift window end

    letterIdxs = {}

    for c in S:
        if c not in letterIdxs:
            letterIdxs[c] = S.rindex(c)
    
    windowStart = 0
    windowEnd = 0
    windows = []

    for i, c in enumerate(S):
        windowEnd = max(windowEnd, letterIdxs[c])
        if i == windowEnd:
            windows.append(windowEnd - windowStart + 1)
            windowStart = windowEnd + 1
        

    return windows
        
if __name__=="__main__":
    S = "ababcbacadefegdehijhklij"
    print(partitionLabels(S))
