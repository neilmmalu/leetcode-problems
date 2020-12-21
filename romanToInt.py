# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Input: s = "III"
# Output: 3

# Input: s = "IV"
# Output: 4

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V = 5, III = 3.

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

def romanToInt(s: str) -> int:
    if not s:
        return 0
    
    romans = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
    
    total = 0
    prev = 0

    for c in reversed(s):
        val = romans[c]
        if prev <= val:
            total += val
            prev = val
        else:
            total += -val
    
    return total

if __name__ == "__main__":
    print(romanToInt("MCMXCIV"))
