// Given an unsorted array A of size N of non-negative integers, find a
// continuous sub-array which adds to a given number S.

#include <iostream>

using namespace std;

class Solution
{
public:
    void subarray(int n, int s, int arr[])
    {
        int till = 0, j = 0;
        for (int i = 0; i < n; i++)
        {
            till += arr[i];
            // cout<<i<<" "<<" "<<arr[i]<<" "<<till<<endl;
            while (till > s)
            {
                till -= arr[j];
                j += 1;
            }

            if (till == s)
            {
                // cout << i << j << " " << n << " " << s << " " << till << endl;
                cout << j + 1 << " " << i + 1 << endl;
                return;
            }
        }
        cout << -1 << endl;
    }
};

int main()
{
    // int T = 0;
    // scanf("%d", &T);
    Solution s;
    // for (int i = 0; i < T; i++)
    // {
    int N = 0, S = 0;
    scanf("%d %d\n", &N, &S);
    int arr[N] = {0};
    for (int i = 0; i < N; i++)
        cin >> arr[i];
    s.subarray(N, S, arr);
    // }

    return 0;
}