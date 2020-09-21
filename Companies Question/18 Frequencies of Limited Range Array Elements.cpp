#include <iostream>
#include <stdlib.h>

using namespace std;

void solver1(int t){  // O(n) time, O(n) space
    while (t--)
    {
        int n;
        cin >> n;
        int arr[n] = {0};
        int temp;

        for (int i = 0; i < n; i++)
        {
            cin >> temp;
            arr[temp - 1]++;
        }
    
        for (int i = 0; i < n; i++)
            cout << arr[i]<<" ";
    
        cout<<endl;
    }
}


int main(int argc, char const *argv[])
{
    int t;
    cin >> t;
    solver(t);

    return 0;
}
