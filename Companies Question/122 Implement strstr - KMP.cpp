#include <iostream>
#include <vector>
using namespace std;

// longest proper prefix(lps) or pi table
vector<int> createLPStable(string pattern, int n)
{
    vector<int> lps(n);
    lps[0] = 0;
    for (int i = 1; i < n; i++)
    {
        if (pattern[0] != pattern[i])
            lps[i] = 0;
        else
        {
            int j = 0;
            while (i < n && pattern[j] == pattern[i])
                lps[i++] = (j++) + 1;
        }
    }
    return lps;
}

// KMP
int strstr(string txt, string pattern)
{
    int n1 = txt.length(), n2 = pattern.length();
    vector<int> pi = createLPStable(pattern, n2);

    // 'i' for text input and j for pattern input 
    int i = 0, j = -1;
    while (i < n1)
    {
        if (txt[i] == pattern[j + 1]) // character matches
            ++j;
        else // character not matches 
        {
            if (j != -1) // pattern index position is not before start/-1
                j = pi[j] - 1;
        }
        ++i;
        
        if (j == n2 - 1) // we reached end of pattern string
            return i - n2;
    }

    return -1;
}

int main(int argc, char const *argv[])
{
    cout << strstr("GeeksForGeeks", "Fr") << endl;
    cout << strstr("GeeksForGeeks", "For") << endl;

    return 0;
}
