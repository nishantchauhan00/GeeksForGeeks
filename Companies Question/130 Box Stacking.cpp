#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
using namespace std;

bool comparator(pair<int, pair<int, int>> a, pair<int, pair<int, int>> b)
{
    return (a.second.first * a.second.second) > (b.second.first * b.second.second);
}

// its a kind of brute force technique by considering all possible ways of
// the box possible
int maxHeight(int height[], int width[], int length[], int n)
{
    // {height, {length, width}}
    vector<pair<int, pair<int, int>>> vec;
    // as we can rotate box, so one bos can have 3 ways
    for (int i = 0; i < n; i++)
    {
        // we can take max first and min later, its just only so that we can
        // easily compare later(length to length and width to width).
        // We can also do this min-max later, but doesn't matter wherever we do
        vec.push_back({height[i], {min(length[i], width[i]), max(length[i], width[i])}});
        vec.push_back({width[i], {min(length[i], height[i]), max(length[i], height[i])}});
        vec.push_back({length[i], {min(height[i], width[i]), max(height[i], width[i])}});
    }

    // sort vector according to top/base/l*w area in decreasing order
    sort(vec.begin(), vec.end(), comparator);

    // storing maximum height of stack possible upto 'i'.
    // initialising with height of box.
    int mh[3 * n];
    for (int i = 0; i < 3 * n; i++)
        mh[i] = vec[i].first;

    // checking current box with previous boxes, if current box can go with
    // previous box, then update max height with maximum of two
    for (int i = 1; i < 3 * n; i++)
        for (int j = 0; j < i; j++)
            if ((vec[i].second.first < vec[j].second.first) && (vec[i].second.second < vec[j].second.second))
                mh[i] = max(mh[i], mh[j] + vec[i].first);

    // just take out the maximum height from 'mh' array
    return *max_element(mh, mh + 3 * n);
}

int main()
{
    int t;
    scanf("%d\n", &t);
    while (t--)
    {
        int n;
        cin >> n;
        int height[n], width[n], length[n];
        cout << maxHeight(height, width, length, n) << endl;
    }
    return 0;
}