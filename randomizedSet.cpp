// Input
//     ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
//     [[], [1], [2], [2], [], [1], [2], []] Output
//         [null, true, false, true, 2, true, false, 2]

//     Explanation
//         RandomizedSet randomizedSet = new RandomizedSet();
// randomizedSet.insert(1);   // Inserts 1 to the set. Returns true as 1 was inserted successfully.
// randomizedSet.remove(2);   // Returns false as 2 does not exist in the set.
// randomizedSet.insert(2);   // Inserts 2 to the set, returns true. Set now contains [1,2].
// randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
// randomizedSet.remove(1);   // Removes 1 from the set, returns true. Set now contains [2].
// randomizedSet.insert(2);   // 2 was already in the set, so return false.
// randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

#include <iostream>
#include <vector>
#include <map>
#include <stdlib.h>

using namespace std;

class RandomizedSet
{
    vector<int> randomSet;
    map<int, int> indexMap;

public:
    /** Initialize your data structure here. */
    RandomizedSet()
    {
    }

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val)
    {
        if (indexMap.find(val) == indexMap.end())
        {
            randomSet.push_back(val);
            indexMap[val] = randomSet.size() - 1;
            return true;
        }
        return false;
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val)
    {
        if (indexMap.find(val) == indexMap.end())
        {
            return false;
        }

        indexMap[randomSet[randomSet.size() - 1]] = indexMap[val];
        swap(randomSet[indexMap[val]], randomSet[randomSet.size() - 1]);
        randomSet.pop_back();
        indexMap.erase(val);
        return true;
    }

    /** Get a random element from the set. */
    int getRandom()
    {
        if (randomSet.size() == 1)
            return randomSet[0];
        return randomSet[rand() % randomSet.size()];
    }
};

int main()
{
    RandomizedSet randomizedSet = RandomizedSet();
    randomizedSet.insert(1);   // Inserts 1 to the set. Returns true as 1 was inserted successfully.
    randomizedSet.remove(2);   // Returns false as 2 does not exist in the set.
    randomizedSet.insert(2);   // Inserts 2 to the set, returns true. Set now contains [1,2].
    randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
    randomizedSet.remove(1);   // Removes 1 from the set, returns true. Set now contains [2].
    randomizedSet.insert(2);   // 2 was already in the set, so return false.
    randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
}