/*
Implement the UndergroundSystem class:

void checkIn(int id, string stationName, int t)
    A customer with a card id equal to id, gets in the station stationName at time t.
    A customer can only be checked into one place at a time.

void checkOut(int id, string stationName, int t)
    A customer with a card id equal to id, gets out from the station stationName at time t.

double getAverageTime(string startStation, string endStation)
    Returns the average time to travel between the startStation and the endStation.
    The average time is computed from all the previous traveling from startStation to endStation that happened directly.

Call to getAverageTime is always valid.
*/

#include <iostream>
#include <string>
#include <map>

using namespace std;

class UndergroundSystem
{

private:
    map<int, pair<string, int>> checkedIn; //k: id, v: { startStation, timeIn }
    map<string, pair<int, int>> stats;

public:
    UndergroundSystem()
    {
    }

    void checkIn(int id, string stationName, int t)
    {
        checkedIn[id] = {stationName, t};
    }

    void checkOut(int id, string endStation, int timeOut)
    {
        auto const &[startStation, timeIn] = checkedIn[id];
        auto &[totalDuration, numTrips] = stats[startStation + ">" + endStation];
        totalDuration += timeOut - timeIn;
        ++numTrips;
    }

    double getAverageTime(string startStation, string endStation)
    {
        auto const [totalDuration, numTrips] = stats[startStation + ">" + endStation];
        return (double)totalDuration / numTrips;
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */

int main()
{

    UndergroundSystem undergroundSystem;
    undergroundSystem.checkIn(45, "Leyton", 3);
    undergroundSystem.checkIn(32, "Paradise", 8);
    undergroundSystem.checkIn(27, "Leyton", 10);
    undergroundSystem.checkOut(45, "Waterloo", 15);
    undergroundSystem.checkOut(27, "Waterloo", 20);
    undergroundSystem.checkOut(32, "Cambridge", 22);
    cout << undergroundSystem.getAverageTime("Paradise", "Cambridge") << endl; // return 14.00000. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
    cout << undergroundSystem.getAverageTime("Leyton", "Waterloo") << endl;    // return 11.00000. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.00000
    undergroundSystem.checkIn(10, "Leyton", 24);
    cout << undergroundSystem.getAverageTime("Leyton", "Waterloo") << endl; // return 11.00000
    undergroundSystem.checkOut(10, "Waterloo", 38);
    cout << undergroundSystem.getAverageTime("Leyton", "Waterloo") << endl;
    return 0;
}