"""
The idea is to consider all events in sorted order. Once the events are in 
sorted order, trace the number of trains at any time keeping track of trains 
that have arrived, but not departed.

For example consider the above example.
arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}

All events are sorted by time.
Total platforms at any time can be obtained by subtracting total departures 
from total arrivals by that time.

platforms: (+1) on arrival, (-1) on departure

 Time      Event Type     Total Platforms Needed 
                               at this Time                               
 9:00       Arrival                  1
 9:10       Departure                0
 9:40       Arrival                  1
 9:50       Arrival                  2
 11:00      Arrival                  3 
 11:20      Departure                2
 11:30      Departure                1
 12:00      Departure                0
 15:00      Arrival                  1
 18:00      Arrival                  2 
 19:00      Departure                1
 20:00      Departure                0

Minimum Platforms needed on railway station 
= Maximum platforms needed at any time 
= 3  
"""


def solver(arrival, departure, n):
    out, curr_platforms = 0, 0
    i, j = 0, 0
    while i < n and j < n:
        if arrival[i] <= departure[j]:
            curr_platforms += 1
            i += 1
        else: # if arrival[i] > departure[j]:
            curr_platforms -= 1
            j += 1

        if curr_platforms > out:
            out = curr_platforms

    return out


T = int(input())
for _ in range(T):
    n = int(input())
    arrival = list(map(int, input().split()))
    departure = list(map(int, input().split()))
    print(solver(sorted(arrival), sorted(departure), n))
