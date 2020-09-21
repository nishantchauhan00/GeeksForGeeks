/*
Given two strings str1 and str2 and below operations that can performed on str1. 
Find minimum number of edits (operations) required to convert ‘str1′ into ‘str2′.
> Insert
> Remove
> Replace

https://leetcode.com/problems/edit-distance/discuss/25895/Step-by-step-explanation-of-how-to-optimize-the-solution-from-simple-recursion-to-DP

this algorithm is called Levenshtein distance 
https://en.wikipedia.org/wiki/Levenshtein_distance
*/
#include <iostream>
#define INT_MAX 2147483647
using namespace std;

/*
// slow, recursion
int solver1(string str1, string str2, int n1, int n2, int i = 0, int j = 0)
{
    // if ends of both word have reached, then no more operations
    if (i == n1 && j == n2) 
        return 0;
    
    // if any of word is left to traverse
    if (i == n1) // insert character of left str2
        return n2 - j;
    if (j == n2) // delete left character of str1
        return n1 - i;

    int res;
    if (str1[i] == str2[j]) // if same string then no operation
        res = solver(str1, str2, n1, n2, i + 1, j + 1);
    else
    {
        // insert, if we insert then index of only second string(str2) will
        // increase, as we inserted the letter of j'th index
        int ins = 1 + solver(str1, str2, n1, n2, i, j + 1);
        // remove
        int rem = 1 + solver(str1, str2, n1, n2, i + 1, j);
        // replace
        int rep = 1 + solver(str1, str2, n1, n2, i + 1, j + 1);
        res = min(ins, min(rem, rep));
    }
    return res;
}
*/

// DP, faster, caching, top down
int helper(int **dp, string str1, string str2, int n1, int n2, int i = 0, int j = 0)
{
    // if ends of both word have reached, then no more operations
    if (i == n1 && j == n2) 
        return 0;
    
    // if any of word is left to traverse
    if (i == n1) // insert character of left str2
        return n2 - j;
    if (j == n2) // delete left character of str1
        return n1 - i;
    
    if (dp[i][j] != -1)
        return dp[i][j];

    if (str1[i] == str2[j]) // if same string then no operation
        dp[i][j] = solver(dp, str1, str2, n1, n2, i + 1, j + 1);
    else
    {
        // insert, if we insert then index of only second string(str2) will
        // increase, as we inserted the letter of j'th index
        int ins = 1 + solver(dp, str1, str2, n1, n2, i, j + 1);
        // remove
        int rem = 1 + solver(dp, str1, str2, n1, n2, i + 1, j);
        // replace
        int rep = 1 + solver(dp, str1, str2, n1, n2, i + 1, j + 1);
        dp[i][j] = min(ins, min(rem, rep));
    }
    return dp[i][j];
}

int solver(string str1, string str2, int n1, int n2)
{
    int **dp;
    dp = new int[n1];
    for (int i = 0; i < n1; i++)
        dp[i] = new int[n2];
    for (int i = 0; i < n1; i++)
        for (int j = 0; j < n2; j++)
            dp[i][j] = -1;
    return helper(dp, str1, str2, n1, n2);
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n1, n2;
        cin >> n1 >> n2;
        string str1, str2;
        cin >> str1 >> str2;

        cout << solver(str1, str2, n1, n2) << endl;
    }
    return 0;
}