'''
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859

Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086
'''

from typing import List


def twoCitySchedCost(costs: List[List[int]]) -> int:
    '''
        Strategy:
        First, check cost of sending everyone to A.
        Then check the price differential between A and B and sort it
        Send the least expensive half of ppl to B (preferably those with refunds)
    '''

    costToA = sum([c[0] for c in costs])

    differential = sorted([B - A for A, B in costs])

    return costToA + sum(differential[:len(costs)//2])


if __name__ == "__main__":
    costs = [[259, 770], [448, 54], [926, 667],
             [184, 139], [840, 118], [577, 469]]
    print(twoCitySchedCost(costs))
