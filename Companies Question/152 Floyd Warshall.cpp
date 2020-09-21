#include <bits/stdc++.h>
#define INF 10000000
using namespace std;
typedef long long ll;

/*
its easy
used to find shortest distance between all nodes

reapeat this for all nodes-
>first consider a node(the current node)
>then update the minimum distance between two nodes, i.e, 
 lets current node considered be 'N'
 min_distance between a and b =  
                    min(
                        min_distance between a and b, 
                        (distance between a to N + distance between N to b)
                    )
 distance for current node N will not be updated in current iteration, it
 will be done in all iteration except current one
*/

void floydWarshall(ll graph[101][101], ll n)
{
    for (int node = 0; node < n; node++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
            {
                if (i == node || j == node)
                    continue;
                else
                    graph[i][j] = min(graph[i][j], (graph[i][node] + graph[node][j]));
            }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (graph[i][j] == INF)
                cout << "INF ";
            else
                cout << graph[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll t;
    cin >> t;
    while (t--)
    {
        ll n;
        cin >> n;
        ll graph[101][101];
        for (ll i = 0; i < n; i++)
        {
            for (ll j = 0; j < n; j++)
            {
                cin >> graph[i][j];
            }
        }

        floydWarshall(graph, n);
    }
    return 0;
}


/*
2
2
0 25
10000000 0
3
0 1 43
1 0 6
10000000 10000000 0
*/