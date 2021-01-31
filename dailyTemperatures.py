'''
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
'''

from typing import List


def dailyTemperatures(T: List[int]) -> List[int]:
    '''
        Strategy:
        Start at the end of the list: last one will always be 0
        Add element to stack
        Compare index to top of stack -> keep popping still stack is lesser
        Add the difference to the result list
    '''

    stack = []
    result = [0] * len(T)

    for i in reversed(range(len(T))):
        while stack and T[i] >= T[stack[-1]]:
            stack.pop()

        if stack:
            result[i] = stack[-1] - i

        stack.append(i)

    return result


if __name__ == "__main__":
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(T))
