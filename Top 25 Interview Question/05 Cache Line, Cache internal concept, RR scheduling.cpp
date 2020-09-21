/*
A cache line is the unit of data transfer between the cache and main memory

I understand that the processor brings data into the cache via cache lines,
which - for instance, on my Atom processor - brings in about 64 bytes at a time,
whatever the size of the actual data being read.
If the cache line containing the byte or word you're loading is not already 
present in the cache, your CPU will request the 64 bytes that begin at the 
cache line boundary (the largest address below the one you need that is multiple
of 64).

Modern PC memory modules transfer 64 bits (8 bytes) at a time, in a burst of 
eight transfers, so one command triggers a read or write of a full cache line 
from memory. (DDR1/2/3/4 SDRAM burst transfer size is configurable up to 64B; 
CPUs will select the burst transfer size to match their cache line size, but 
64B is common)

As a rule of thumb, if the processor can't forecast a memory access (and 
prefetch it), the retrieval process can take ~90 nanoseconds, or ~250 clock 
cycles (from the CPU knowing the address to the CPU receiving data).

By contrast, a hit in L1 cache has a load-use latency of 3 or 4 cycles, and a 
store-reload has a store-forwarding latency of 4 or 5 cycles on modern x86 CPUs. 
Things are similar on other architectures.

The following particular aspects are of high importance to optimize caching:
1. Temporal locality: when a given memory location was accessed, it is likely 
that the same location is accessed again in the near future. Ideally, this 
information will still be cached at that point.
2. Spatial locality: this refers to placing related data close to each other. 
Caching happens on many levels, not just in the CPU. For example, when you read 
from RAM, typically a larger chunk of memory is fetched than what was specifically 
asked for because very often the program will require that data soon. HDD caches 
follow the same line of thought. Specifically for CPU caches, the notion of 
cache lines is important.


Convoy Effect is phenomenon associated with the First Come First Serve (FCFS) 
algorithm, in which the whole Operating System slows down due to few slow 
processes.


https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/
*/
#include <iostream>
#include <vector>
#include <queue>
#include <stdlib.h>

using namespace std;

class Solution
{
public:
    // quantum = 1 unit
    void roundrobin(queue<int> processlist, int bursttime[])
    {
        int n = 3;
        int waitingtime[n] = {0}, w[n] = {0};

        cout<<"Process Order:\t";
        while (!processlist.empty())
        {
            int process = processlist.front();
            processlist.pop();

            bursttime[process - 1] -= 1;
            cout << "P" << process << " ";

            waitingtime[process - 1] += w[process - 1];
            w[process - 1] = 0;
            for (int i = 0; i < n; i++)
                if (i + 1 != process)
                    w[i] += 1;

            if (bursttime[process - 1] > 0)
                processlist.push(process);
        }

        int averagewaitingtime = 0;
        cout << "\nWaiting Time: \t";
        for (int i = 0; i < n; i++)
        {
            averagewaitingtime += waitingtime[i];
            cout << "|   P" << (i + 1) << ": " << waitingtime[i] << "   ";
        }

        cout << "\nAverage Waiting Time: " << averagewaitingtime<<endl;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    queue<int> processlist;
    processlist.push(1);
    processlist.push(2);
    processlist.push(3);
    int bursttime[] = {3, 4, 3};
    s.roundrobin(processlist, bursttime);

    return 0;
}
