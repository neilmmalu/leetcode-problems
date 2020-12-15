# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.

from typing import List
import heapq

def topKFrequent(words: List[str], k: int) -> List[str]:
    # Strategy:
    # Add to map of word count
    # Sort word count by value
    # For top k ones, sort by key
    # This is the nlogn solution

    wordCount = {}

    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1


    # frequents = [words[0] for words in sorted(wordCount.items(), key=lambda tup: (-tup[1], tup[0]))]

    # return frequents[:k]

    # If we create a max heap of size k, this will be reduced to nlogk
    # O(N) time to get frequencies
    # O(log k) time to add each one to the heap => O(Nlogk)

    heap = [(-count, word) for (word, count) in wordCount.items()]
    heapq.heapify(heap)

    return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == "__main__":
    input = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    print(topKFrequent(input, k))
