# On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.

# Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

# You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.

# A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.

# Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.

from typing import List
from collections import deque


def exclusiveTime(n: int, logs: List[str]) -> List[int]:
    if not logs:
        return 0

    totalTimes = {i: 0 for i in range(n)}

    stack = deque()

    for log in logs:
        funcId, op, time = log.split(":")

        if stack:
            oldFuncId, oldTime = stack.pop()
            if op == "start":
                totalTimes[oldFuncId] += int(time) - oldTime
                stack.append((oldFuncId, oldTime))
                stack.append((int(funcId), int(time)))
            else:
                totalTimes[oldFuncId] += int(time) - oldTime + 1
                if stack:
                    oldFuncId, oldTime = stack.pop()
                    stack.append((oldFuncId, int(time) + 1))
        else:
            stack.append((int(funcId), int(time)))

    return list(totalTimes.values())


if __name__ == "__main__":
    n = 2
    logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]

    n = 1
    logs = ["0:start:0", "0:start:2", "0:end:5",
            "0:start:6", "0:end:6", "0:end:7"]
    n = 2
    logs = ["0:start:0", "0:start:2", "0:end:5",
            "1:start:6", "1:end:6", "0:end:7"]

    n = 2
    logs = ["0:start:0", "0:start:2", "0:end:5",
            "1:start:7", "1:end:7", "0:end:8"]

    n = 1
    logs = ["0:start:0", "0:end:0"]
    print(exclusiveTime(n, logs))
