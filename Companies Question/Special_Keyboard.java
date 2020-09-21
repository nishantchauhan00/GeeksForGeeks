import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.*;

/**
 * this problem has a pattern of actions which is going to lead to the highest
 * score which is not so hard to see & prove formally. Basically it is 
 * A, A, A, [A,] S, C, P, P, P, S, C, P, P, P, ..., S, C, P, P[, P]. 
 * max(4*maxA(n-5), 3*maxA(n-4))
 * 
 * Special_Keyboard
 */
public class Special_Keyboard {

    public static int maxA1(int N, int M, int copied) {
        int x = M;

        // printing A
        if (N > 0)
            x = Math.max(x, maxA1(N - 1, M + 1, copied));

        // just paste
        if (N > 0)
            x = Math.max(x, maxA1(N - 1, M + copied, copied));

        // select+copy+paste
        if (N > 2)
            x = Math.max(x, maxA1(N - 3, 2 * M, M));

        return x;
    }

    public static int maxA(int n) {
        if (n < 7)
            return n;

        // it is going from last, it is bottom up approach
        // 1. Printing last buffer onces, we need three key strokes, 
        //    so 2*max(n-3)
        // 2. Printing last buffer thrice, we need 2 keystroke for copy +
        //    2 for printing, 2+2=4, so 3*max(n-4)
        // 3. Similar approach for printing last buffer four times
        return Math.max(4 * maxA(n - 5), 3 * maxA(n - 4));
    }

    public static void main(String[] args) {
        int t;
        Scanner st = new Scanner(System.in);

        t = st.nextInt();

        while (t > 0) {
            int n = st.nextInt();
            System.out.println(maxA2(n));

            t--;
        }

        st.close();
    }
}
