#include <iostream>
#include <stdlib.h>
#include <vector>
#include <math.h>
#include <unordered_map>
using namespace std;

/*
https://practice.geeksforgeeks.org/problems/circle-of-strings/0/

Given an array of strings A[], determine if the strings can be chained 
together to form a circle. A string X can be chained together with another 
string Y if the last character of X is same as first character of Y. 
If every string of the array can be chained, it will form a circle.

For eg for the array arr[] = {"for", "geek", "rig", "kaf"} the answer will 
be Yes as the given strings can be chained as "for", "rig", "geek" and "kaf".
*/

bool helper(bool vis[], string curr, string arr[], int count, int n)
{
    if (count == n)
    {
        if (curr[0] == curr[curr.size() - 1])
        {
            // cout << curr << "  " << endl;
            return true;
        }
        return false;
    }

    for (int i = 0; i < n; i++)
    {
        if (vis[i] || curr[curr.size() - 1] != arr[i][0])
            continue;

        vis[i] = true;
        bool solved = helper(vis, curr + " " + arr[i], arr, count + 1, n);
        if (solved)
            return true;
        vis[i] = false;
    }

    return false;
}

int solver(string arr[], int n)
{
    bool vis[n] = {false};
    bool solved = false;
    for (int i = 0; i < n; i++)
    {
        vis[i] = true;
        solved = helper(vis, arr[i], arr, 1, n);
        if (solved)
            break;
        vis[i] = false;
    }
    return solved;
}

int main(int argc, char const *argv[])
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        string arr[n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];
        cout << solver(arr, n) << endl;
    }
    return 0;
}
