/*
Design a Leaderboard class, which has 3 functions:

addScore(playerId, score): 
    Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
top(K): 
    Return the score sum of the top K players.
reset(playerId): 
    Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.

Initially, the leaderboard is empty.
*/

#include <iostream>
#include <map>
#include <set>

using namespace std;

class Leaderboard
{
    map<int, int> scores;           //k: playerId, v: totalScore
    map<int, set<int>> leaderboard; //k: score, v: set of players at that score
public:
    Leaderboard()
    {
    }

    void addScore(int playerId, int score)
    {
        auto &totalScore = scores[playerId];
        int prevScore = totalScore;
        totalScore += score;

        auto &prevSet = leaderboard[prevScore];
        auto &currSet = leaderboard[totalScore];

        prevSet.erase(playerId);
        currSet.insert(playerId);
    }

    int top(int K)
    {
        int sum = 0;
        auto it = leaderboard.rbegin();

        while (it != leaderboard.rend() && K)
        {
            auto count = it->second.size();
            auto score = it->first;

            if (K >= count)
            {
                K -= count;
                sum += count * score;
            }
            else
            {
                sum += K * score;
                K = 0;
            }

            ++it;
        }

        return sum;
    }

    void reset(int playerId)
    {
        auto const totalScore = scores[playerId];
        auto &prevSet = leaderboard[totalScore];
        prevSet.erase(playerId);
        scores.erase(playerId);
    }
};