# You have an array of logs.  Each log is a space delimited string of words.

# For each log, the first word in each log is an alphanumeric identifier.  Then, either:

# Each word after the identifier will consist only of lowercase letters, or
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

# Return the final order of the logs.

# Input: logs = ["dig1 8 1 5 1", "let1 art can",
#                "dig2 3 6", "let2 own kit dig", "let3 art zero"]
# Output: ["let1 art can", "let3 art zero",
#          "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

from typing import List
def reorderLogFiles(logs: List[str]) -> List[str]:

    # Split digit and letter logs into different lists
    # Then use a key setter to sort letter logs based on the new key
    # Concat sorted letter logs with digit logs and return

    digitLogs = []
    letterLogs = []

    # Iterate through main list
    for log in logs:
        # If the word is alphabetic, add to letter logs
        if log.split()[1].isalpha():
           letterLogs.append(log)
        else:
            digitLogs.append(log)

    def keySetter(log):
        splitLog = log.split()
        identifier, words = splitLog[0], splitLog[1: ]
        return ' '.join(words) + ' ' + identifier

    letterLogs.sort(key = keySetter)
    return letterLogs + digitLogs


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can",
               "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    
    sortedLogs = reorderLogFiles(logs)
    print(sortedLogs)

