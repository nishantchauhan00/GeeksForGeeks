#include <iostream>
#include <vector>
using namespace std;

/*
Give a N*N square matrix, return an array of its anti-diagonals. Look at the 
example for more details.

For Example:
If the matrix is:
1 2 3
4 5 6
7 8 9

The output should Return the following :
[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]
i.e print the elements of array diagonally.
*/

vector<vector<int>> solver(vector<vector<int>> arr, int n)
{
    vector<vector<int>> out;
    for (int j = 0; j < n; j++)
    {
        vector<int> out1;
        int i = 0, j1 = j;
        while (i < n and j >= 0)
            out1.push_back(arr[i++][j--]);
        out.push_back(out1);
        j = j1;
    }

    for (int i = 1; i < n; i++)
    {
        vector<int> out1;
        int j = n - 1, i1 = i;
        while (i < n and j >= 0)
            out1.push_back(arr[i++][j--]);
        out.push_back(out1);
        i = i1;
    }

    return out;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<vector<int>> arr(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                cin >> arr[i][j];

        vector<vector<int>> res = solver(arr, n);
        for (vector<int> vec : res)
            for (int i = 0; i < vec.size(); i++)
                cout << vec[i] << " ";

        cout << endl;
    }
    return 0;
}