#include <bits/stdc++.h>
using namespace std;

// https://www.geeksforgeeks.org/job-sequencing-problem/

struct job
{
    int id, deadline, profit;
    job(int i, int d, int p) : id(i), deadline(d), profit(p){}
};

// it takes one unit of time to complete a job
void solver(map<int, job *> jobs, int n, int last_deadline)
{
    int jobs_sequence[last_deadline] = {0};
    for (auto it = jobs.begin(); it != jobs.end(); it++)
    {
        int i = it->second->deadline - 1;
        // if there is no job present at given deadline
        if (jobs_sequence[i] == 0)
            jobs_sequence[i] = it->first;
        else
        {
            int j = i;
            // check if there is any empty slot before the deadline
            for (; i >= 0; --i)
                if (jobs_sequence[i] == 0)
                {
                    jobs_sequence[i] = it->first;
                    break;
                }

            // if it there is no empty slot then it will not get placed
            // and 'i' will become -1
            if (i == -1)
            {
                int min_index = 0;
                for (i = 0; i <= j; i++)
                    if (jobs[jobs_sequence[i]]->profit < jobs[jobs_sequence[min_index]]->profit)
                        min_index = i;

                int prev_profit = jobs[jobs_sequence[min_index]]->profit;
                if (prev_profit < it->second->profit)
                    jobs_sequence[min_index] = it->second->id;
            }
        }
    }

    int jobs_total = 0, profit_total = 0;
    for (int i = 0; i < last_deadline; i++)
        if (jobs_sequence[i] != 0)
        {
            profit_total += jobs[jobs_sequence[i]]->profit;
            ++jobs_total;
        }

    // number of jobs, total profit
    cout << jobs_total << " " << profit_total << endl;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, last_deadline = 0;
        cin >> n;
        map<int, job *> jobs;
        for (int i = 0; i < n; i++)
        {
            int id, deadline, profit;
            cin >> id >> deadline >> profit;
            last_deadline = max(last_deadline, deadline);
            job *njob = new job(id, deadline, profit);
            jobs[id] = njob;
        }
        solver(jobs, n, last_deadline);
    }
    return 0;
}
