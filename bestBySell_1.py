# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price=1) and sell on day 5 (price=6), profit = 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.

# Input: [7, 6, 4, 3, 1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

from typing import List

def maxProfit(prices: List[int]) -> int:
    # Strategy: Put diff of all indices in an array. If we get a profit, move right. If we get a loss, move both left and right
    # Return the max of the diff array
    N = len(prices)
    if N < 2:
        return 0

    profits = []
    profits.append(0)

    i = 0
    j = 1

    while i < N and j < N:
        diff = prices[j] - prices[i]
        profits.append(diff)

        if diff < 0:
            i = j
        j += 1
    
    return max(profits)

if __name__ == "__main__":
    input = [7, 1, 5, 3, 6, 4]
    print(maxProfit(input))

