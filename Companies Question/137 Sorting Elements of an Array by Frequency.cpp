#include <bits/stdc++.h>
using namespace std;

unordered_map<int, int> hmap;

bool comparator(pair<int, int> a, pair<int, int> b){
    if (a.first != b.first) // if frequency of one is greater than other
        return a.first > b.first;
    else // if frequencies of both are equal
        return a.second < b.second;
}

vector<pair<int, int>> sortingByFrequency()
{
    // (frequency, integer)
    vector<pair<int, int>> vec;
    for (auto it = hmap.begin(); it != hmap.end(); it++)
        vec.push_back(pair<int, int>(it->second, it->first));

    sort(vec.begin(), vec.end(), comparator);

    return vec;
}

int main(int argc, char const *argv[])
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        hmap.clear();
        while(n--){
            int el;
            cin >> el;
            hmap[el]++;
        }

        vector<pair<int, int>> vec = sortingByFrequency();

        for (auto it: vec)
            while(it.first-- > 0)
                cout << it.second << " ";
        cout << endl;
    }
    return 0;
}