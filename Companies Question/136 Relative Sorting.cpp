#include <bits/stdc++.h>
using namespace std;

// using map becuase in it we will get elements in ordered form according to
// their value so that it can be easily used to return element in order which
// are not present in array A2
map<int, int> hmap;

int *relSorting(int A2[], int m, int n) {
    int ai = 0;
    int *A1 = new int[m];
    for(int i=0; i<n; i++)
    {
        if (hmap.find(A2[i]) != hmap.end()){
            for(int j = 0; j < hmap[A2[i]]; j++, ai++)
                A1[ai] = A2[i];
            hmap[A2[i]] = 0;
        }
    }
    
    for(auto it = hmap.begin(); it != hmap.end(); it++){
        if (it->second != 0){
            for(int j = 0; j < it->second; j++, ai++)
                A1[ai] = it->first;
        }
    }

    return A1;
}

int main(int argc, char const *argv[]) {
    int t;
    cin >> t;
    while(t--) {
        int m, n;
        cin >> m >> n;
        int A2[n];
        hmap.clear();
        for(int i=0; i<m; i++){
            int el;
            cin >> el;
            hmap[el] += 1;
        }
        for(int i=0; i<n; i++)
            cin >> A2[i];
            
        int *A1 = relSorting(A2, m, n);
        
        for(int i=0; i<m; i++)
            cout << A1[i] << " ";
        cout << endl;
    }
    return 0;
}