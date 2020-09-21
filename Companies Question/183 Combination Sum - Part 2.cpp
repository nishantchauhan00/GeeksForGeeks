#include <vector>
#include <iostream>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution
{
public:
    void helper(int i, int csum, int target, int n, vector<vector<int>> &out, vector<int> &curr, vector<int> &arr)
    {
        cout<<i<<" "<<csum<<"     ";
        for(int el: curr)
            cout<<el<<" ";
        cout<<endl;

        if (csum == target)
        {
            out.push_back(curr);
            return;
        }

        for (int j = i; j < n; j++)
        {
            if (j > i && arr[j] == arr[j - 1])
                continue;

            if (csum + arr[j] > target)
                break;
                
            curr.push_back(arr[j]);
            helper(j + 1, csum + arr[j], target, n, out, curr, arr);
            curr.pop_back();
        }
    }

    vector<vector<int>> combinationSum2(vector<int> &candidates, int target)
    {
        vector<vector<int>> out;
        vector<int> curr;

        sort(candidates.begin(), candidates.end());
        helper(0, 0, target, candidates.size(), out, curr, candidates);

        return out;
    }
};

int main(int argc, char const *argv[])
{
    int t;
    cin >> t;
    while (t--)
    {
        int N, target;
        cin >> target;
        cin >> N;
        vector<int> arr(N);
        for (int i = 0; i < N; i++)
            cin >> arr[i];

        Solution ob;
        vector<vector<int>> out;
        out = ob.combinationSum2(arr, target);
        for (int i = 0; i < out.size(); i++)
        {
            for (int j = 0; j < out[i].size(); j++)
            {
                cout << out[i][j] << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
    return 0;
}

/*
3
8
7
10 1 2 7 6 1 5
5
5
2 5 2 1 2
27
55
14 6 25 9 30 20 33 34 28 30 16 12 31 9 9 12 34 16 25 32 8 7 30 12 33 20 21 29 24 17 27 34 11 17 30 6 32 21 27 17 16 8 24 12 12 28 11 33 10 32 22 13 34 18 12


Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]


Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

*/