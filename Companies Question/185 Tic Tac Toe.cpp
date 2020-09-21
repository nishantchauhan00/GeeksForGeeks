#include <bits/stdc++.h>
using namespace std;
/*
To find the validity of a given board, we could first think about the cases 
where the board is invalid.

*Since X starts first, x_count >= o_count. So if o_count > x_count, we can 
return False
*Since the players take turns, we could also return False if x_count-o_count > 1

After the corner cases, this is the algorithm used:
1. If player O has a winning condition, also check the following:
    a) If player X also has a winning condition, return False
    b) If x_count != o_count , return False (Since player O always plays 
       second, it has to meet this condition always)

2. If player X has a winning condition, check the following:
    a) If x_count != o_count + 1, return False (Since player X plays the first 
       move, if player X wins, the player X's count would be 1 more than player 
       O)
*/


class Solution{   
public:
    bool isValid(char board[9]){
        int x = 0, o = 0;
        for(int i=0; i<9; i++){
            if (board[i] == 'X')
                ++x;
            else
                ++o;
        }
        if ((o > x) or (x-o > 1)) 
            return false;
        
        bool x_wins = false, y_wins= false;
        // check rows
        for(int i = 0; i<3; i++)
            if((board[i*3] == board[i*3 + 1]) && (board[i*3 +1] == board[i*3+2])){
                if (board[i*3] == 'X')
                    x_wins =  true;
                else
                    y_wins = true;
            }
            
        // check columns
        for(int i = 0; i<3; i++)
            if((board[i] == board[i + 3]) && (board[i + 3] == board[i + 6])){
                if (board[i] == 'X')
                    x_wins =  true;
                else
                    y_wins = true;
            }
        
        // check diagonals
        if ((board[0] == board[4]) && (board[4] == board[8]))
            {
                if (board[0] == 'X')
                    x_wins =  true;
                else
                    y_wins = true;
            }

        if ((board[2] == board[4]) && (board[4] == board[6]))
            {
                if (board[2] == 'X')
                    x_wins =  true;
                else
                    y_wins = true;
            }

        if (x_wins && y_wins)
            return false;
        else if (y_wins && x != o)
            return false;
        else if (x_wins && x != o + 1)
            return false;
        else
            return true;
    }
};

int main() {
    int t;
    cin >> t;
    while (t--) {
        char board[9];
        for (int i = 0; i < 9; i++) {
            cin >> board[i];
        }
        Solution ob;
        auto ans = ob.isValid(board);
        cout << (ans ? "Valid\n" : "Invalid\n");
    }
    return 0;
}