# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Follow up: Could you solve it without converting the integer to a string?

# Input: x = 121
# Output: true

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads - 121. From right to left, it becomes 121-. Therefore it is not a palindrome.

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    div = 1
    y = x
    while y > 9:
        y //= 10
        div *= 10
    
    while div > 1:
        if x//div != x%10:
            return False
        x = (x%div) // 10
        div //= 100

    return True 

if __name__ == "__main__":
    print(isPalindrome(11111))
