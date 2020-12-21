# Given a 32-bit signed integer, reverse digits of an integer.

# Note:
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# Input: x = 123
# Output: 321

# Input: x = -123
# Output: -321

def reverse(x : int) -> int:
    neg = False
    if x < 0:
        neg = True
        x = abs(x)
    
    ans = 0
    div = 1
    y = x

    while y > 9:
        div *= 10
        y //= 10
    
    while x != 0:
        ans += (x % 10) * div
        x = x//10
        div = div//10
    
    return (-ans if neg else ans) if ans.bit_length() < 32 else 0

if __name__ == "__main__":
    print(reverse(-93020129492198430))
