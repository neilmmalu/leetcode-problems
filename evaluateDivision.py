'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
'''

from typing import List
from collections import deque


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

    graph = {}

    def createGraph(equations, values):

        def addEdge(f, t, val):
            if f in graph:
                graph[f].append((t, val))
            else:
                graph[f] = [(t, val)]

        for vertices, val in zip(equations, values):
            f, t = vertices
            addEdge(f, t, val)
            addEdge(t, f, 1/val)

    def findPath(query):
        src, dest = query

        if src not in graph or dest not in graph:
            return -1

        q = deque()

        q.append((src, 1))

        visited = set()

        while q:
            curr, dist = q.popleft()

            if curr == dest:
                return dist

            visited.add(curr)

            for n, val in graph[curr]:
                if n not in visited:
                    q.append((n, dist * val))

        return -1

    createGraph(equations, values)
    return [findPath(q) for q in queries]


if __name__ == "__main__":
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    print(calcEquation(equations, values, queries))