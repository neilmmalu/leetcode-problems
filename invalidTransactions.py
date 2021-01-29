'''
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

'''

from typing import List


def invalidTransactions(transactions: List[str]) -> List[str]:
    invalids = []

    for i, t1 in enumerate(transactions):
        name1, time1, amount1, city1 = t1.split(',')
        if int(amount1) > 1000:
            invalids.append(t1)
            continue
        for j, t2 in enumerate(transactions):
            if i != j:
                name2, time2, amount2, city2 = t2.split(',')
                if name1 == name2 and city1 != city2 and abs(int(time1) - int(time2)) <= 60:
                    invalids.append(t1)
                    break
    return invalids
