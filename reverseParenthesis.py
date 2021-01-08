# You are given a string s that consists of lower case English letters and brackets.

# Reverse the strings in each pair of matching parentheses, starting from the innermost one.

# Your result should not contain any brackets.

# Input: s = "(abcd)"
# Output: "dcba"

# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.

# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

# Input: s = "a(bcdefghijkl(mno)p)q"
# Output: "apmnolkjihgfedcbq"

from collections import deque


def reverseParentheses(s: str) -> str:
    if not s:
        return ''

    stack = deque()

    pairs = {}

    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        if c == ")":
            p = stack.pop()
            pairs[p], pairs[i] = i, p

    i = 0
    direction = 1
    result = ""
    while i < len(s):
        c = s[i]
        if c in '()':
            i = pairs[i]
            direction *= -1
        else:
            result += c
        i += direction

    return result


if __name__ == "__main__":
    s = "(ed(et(oc))el)"
    print(reverseParentheses(s))
