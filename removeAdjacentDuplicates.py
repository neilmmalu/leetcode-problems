'''
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.
'''


def removeDuplicates(s: str, k: int) -> str:
    stack = [['1', 0]]
    for c in s:
        if stack[-1][0] == c:
            stack[-1][1] += 1

            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([c, 1])

    return ''.join([c*count for c, count in stack])


if __name__ == "__main__":
    print(removeDuplicates("pbbcggttciiippooaais", 2))
