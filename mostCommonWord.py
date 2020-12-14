# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

# Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

# Input:
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice(and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored(even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.

import re
from typing import List

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    # Strategy:
    # Replace all punctuations with spaces and strip the string
    # Convert paragraph to list
    # Iterate through list and add to dict with count
    # Get key in dict with highest value
    
    paragraph = re.sub(r'[^\w\s]', ' ', paragraph)

    listOfAllWords = paragraph.split()

    wordCount = {}

    for word in listOfAllWords:
        word = word.lower()
        if word not in banned:
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1
    
    maxVal = 0
    maxKey = ""
    for key, val in wordCount.items():
        if val > maxVal:
            maxVal = val
            maxKey = key
    
    return maxKey
    

if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(mostCommonWord(paragraph, banned))

