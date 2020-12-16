# Given two words(beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

# Output: 5

# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot", "dot", "dog", "lot", "log"]

# Output: 0

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

from typing import List
from collections import deque, defaultdict

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    # Strategy:
    # BFS:
    # From begin word, change a char to match endWord: if it exists in the list, add to queue
    # To get perfect solution, create dict with all combs at the start instead of doing it in the BFS loop
    
    if endWord not in wordList:
        return 0

    q = deque()
    q.append((beginWord, 1))

    allCombs = defaultdict(list)
    for word in wordList:
        for i in range(len(beginWord)):
            allCombs[word[:i] + "*" + word[i+1:]].append(word)
    

    inQueue = { beginWord: True }

    while q:
        word, dist = q.popleft()
        
        for i in range(len(word)):
            nextWord = word[:i] + "*" + word[i+1:]

            for comb in allCombs[nextWord]:
                if comb == endWord:
                    return dist + 1
                if comb not in inQueue:
                    inQueue[comb] = True
                    q.append((comb, dist + 1))
            allCombs[nextWord] = []
    return 0
    

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(ladderLength(beginWord, endWord, wordList))

