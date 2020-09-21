#include <iostream>
#include <stdlib.h>
#include <vector>
#include <math.h>
#include <unordered_map>
#include "../utils/LinkedList.hpp"
using namespace std;

// recursion - giving tle
int lps1(vector<int> vec, int i, int j)
{
    // only one number present
    if (i == j)
        return 1;

    // only two number present
    if ((vec[i] == vec[j]) && (i + 1 == j))
        return 2;

    if (vec[i] == vec[j])
        return 2 + lps1(vec, i + 1, j - 1);

    return max(lps1(vec, i + 1, j), lps1(vec, i, j - 1));
}


///////////////////////////////////////////////////////////
// expand around center
int expand(vector<int> vec, int l, int r, int n)
{
    while (l >= 0 && r < n && vec[l] == vec[r])
    {
        --l;
        ++r;
    }
    return r - l;
}

int lps(vector<int> vec, int n)
{
    int out = 0;
    for (int i = 0; i < n; i++)
    {
        int l1 = expand(vec, i, i, n);
        int l2 = expand(vec, i, i + 1, n);
        out = max(out, max(l1, l2));
    }

    return out - 1;
}


/*The function below returns an int denoting
the length of the longest palindrome list. */
int maxPalindrome(node *head)
{
    // first load ll in array
    vector<int> vec;
    for (; head; head = head->next)
        vec.push_back(head->val);

    // return lps1(vec, 0, vec.size()-1);
    return lps(vec, vec.size());
}

int main(int argc, char const *argv[])
{
    LinkedList ll;
    node *head;

    int arr[] = {2, 3, 7, 3, 2, 12, 24};
    head = ll.loadList(arr, 7);
    cout << maxPalindrome(head) << endl;

    int arr1[] = {12, 4, 4, 3, 14};
    head = ll.loadList(arr1, 5);
    cout << maxPalindrome(head) << endl;

    // 5 2

    return 0;
}
