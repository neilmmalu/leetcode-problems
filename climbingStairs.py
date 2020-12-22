# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


def climbStairs(n: int) -> int:
    if n < 1:
        return 1

    arr = [None]*(n+1)
    arr[0] = 1
    arr[1] = 1

    for i in range(2, n+1):
        arr[i] = arr[i-2] + arr[i-1]

    return arr[n]


if __name__ == "__main__":
    print(climbStairs(15))
