#include <iostream>
#include <stack>
using namespace std;
// https://www.geeksforgeeks.org/length-of-the-longest-valid-substring/

int solver1(string inp)
{
    stack<int> st;
    int n = inp.size(), count = 0, curr = 0;
    for (int i = 0; i < n; i++)
    {
        if (inp[i] == '(')
        {
            st.push(curr);
            curr = 0;
        }
        else if (!st.empty() && inp[i] == ')')
        {
            curr += st.top() + 2;
            st.pop();
            count = max(curr, count);
        }
        else if (st.empty() && inp[i] == ')')
        { // invalid parentheses case
            curr = 0;
        }
    }

    return count;
}

int solver(string inp)
{
    int result = 0, n = inp.size();
    int left = 0, right = 0;

    // left to right
    for (int i = 0; i < n; ++i)
    {
        if (inp[i] == '(')
            ++left;
        else
            ++right;
        
        if (left == right)
            result = max(result, 2*left);
        else if (right > left) // invalid parentheses case
            left = right = 0;
    }

    // right to left
    for (int i = n-1; i >= 0; --i)
    {
        if (inp[i] == '(')
            ++left;
        else
            ++right;
        
        if (left == right)
            result = max(result, 2*left);
        else if (left > right) // invalid parentheses case
            left = right = 0;
    }

    return result;
}

int main()
{
    int T;
    cin >> T;

    while (T--)
    {
        string inp;
        cin >> inp;

        cout << solver(inp) << endl;
    }
    return 0;
}