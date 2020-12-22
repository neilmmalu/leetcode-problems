# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Input: coins = [2], amount = 3
# Output: -1

from typing import List
from collections import deque


def coinChange(coins: List[int], amount: int) -> int:
    '''
        Strategy:
        D.P:
        minCoins[i] = min(minCoins[i], minCoins[amount-coin] + 1)

        BFS:
        Add coin and total as tuple. Keep adding till all amounts visited.
    '''
    if not amount:
        return 0

    # minCoins = [0] + [float("inf")]*amount

    # for coin in coins:
    #     for i in range(amount + 1):
    #         if i >= coin:
    #             minCoins[i] = min(minCoins[i - coin] + 1, minCoins[i])
    # return minCoins[amount] if minCoins[amount] < float("inf") else -1

    q = deque()
    q.append((0, 0))
    visited = [True] + [False]*amount

    while q:
        totalCoins, currVal = q.popleft()
        totalCoins += 1
        for coin in coins:
            totalVal = currVal + coin
            if totalVal == amount:
                return totalCoins

            if totalVal < amount:
                if not visited[totalVal]:
                    visited[totalVal] = True
                    q.append((totalCoins, totalVal))

    return -1


if __name__ == "__main__":
    coins = [1, 2, 5, 10]
    amount = 15
    print(coinChange(coins, amount))
