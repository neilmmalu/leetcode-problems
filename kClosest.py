# We have a list of points on the plane.  Find the K closest points to the origin(0, 0).

# (Here, the distance between two points on a plane is the Euclidean distance.)

# You may return the answer in any order.  The answer is guaranteed to be unique(except for the order that it is in.)

# Input: points = [[1, 3], [-2, 2]], K = 1
# Output: [[-2, 2]]
# Explanation:
# The distance between(1, 3) and the origin is sqrt(10).
# The distance between(-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just[[-2, 2]].

# Input: points = [[3, 3], [5, -1], [-2, 4]], K = 2
# Output: [[3, 3], [-2, 4]]
# (The answer[[-2, 4], [3, 3]] would also be accepted.)

from typing import List
from collections import OrderedDict

def kClosest(points: List[List[int]], K: int) -> List[List[int]]:
    # Strategy: Calculate the dist and add to dict
    # If dict with same key exists, append the point to the list

    distDict = OrderedDict()

    for point in points:
        dist = point[0]*point[0] + point[1]*point[1]
        if dist in distDict:
            distDict[dist].append(point)
        else:
            distDict[dist] = [point]
    
    distDict = dict(sorted(distDict.items()))
    closest = sum(distDict.values(), [])
    return closest[:K]

if __name__ == "__main__":
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    print(kClosest(points, K))
