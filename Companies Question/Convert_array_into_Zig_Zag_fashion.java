/**
 * Convert_array_into_Zig_Zag_fashion Given an array A (distinct elements)
 * of size N. Rearrange the elements of array in zig-zag fashion. The converted
 * array should be in form a < b > c < d > e < f. The relative order of elements
 * is same in the output i.e you have to iterate on the original array only.
 */
import java.util.*;

public class Convert_array_into_Zig_Zag_fashion {
    static void swap(int[] pat, int i) {
        int tmp = pat[i];
        pat[i] = pat[i + 1];
        pat[i + 1] = tmp;
    }

    public static void main(String[] args) {
        int t;
        Scanner scan = new Scanner(System.in);

        t = scan.nextInt();

        while (t > 0) {

            int n = scan.nextInt();
            int[] pat = new int[n];

            for (int i = 0; i < n; i++) {
                pat[i] = scan.nextInt();
            }

            for (int i = 0; i < n - 1; i++) {
                if (i % 2 == 0) {
                    if (pat[i] > pat[i + 1])
                        swap(pat, i);
                } else {
                    if (pat[i] < pat[i + 1])
                        swap(pat, i);
                }
            }

            for (int i = 0; i < n; i++)
                System.out.print(pat[i] + " ");
            System.out.println("");

            t--;
        }

        scan.close();
    }
}