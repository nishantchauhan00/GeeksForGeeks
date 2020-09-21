#include <bits/stdc++.h>
using namespace std;
// The Median is the "middle" of a sorted list of numbers.
// https://www.mathsisfun.com/median.html

int getMedian(priority_queue<int> &pq1, priority_queue<int, vector<int>, greater<int>> &pq2, int num)
{
    // insert in pq1 if its empty or its maximum/top element is greater than
    // element to be inserted, else in pq2
    if (pq1.empty() || num < pq1.top())
        pq1.push(num);
    else
        pq2.push(num);

    // settle both if difference in number of elements is greater than 1 
    if (pq1.size() > pq2.size() + 1)
    {
        pq2.push(pq1.top());
        pq1.pop();
    }
    else if (pq1.size() + 1 < pq2.size())
    {
        pq1.push(pq2.top());
        pq2.pop();
    }

    // get median
    int median;
    if (pq1.size() == pq2.size())
        median = (pq1.top() + pq2.top()) / 2;
    else if (pq1.size() > pq2.size())
        median = pq1.top();
    else
        median = pq2.top();
    return median;
}

int main()
{
    int n;
    cin >> n;
    // median will be present in one or maybe both
    // (if two elements are middle then take avg)
    // pq1=stores number before median
    // pq2=stores number after median
    priority_queue<int> pq1; // max heap
    priority_queue<int, vector<int>, greater<int>> pq2; // min heap

    while (n--)
    {
        int num;
        cin >> num;
        cout << getMedian(pq1, pq2, num) << endl;
    }
    return 0;
}

