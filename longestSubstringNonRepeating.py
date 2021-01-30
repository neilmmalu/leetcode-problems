'''

Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''


def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    maxLength = start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        used[c] = i

    return maxLength


if __name__ == "__main__":
    print(lengthOfLongestSubstring(" "))
