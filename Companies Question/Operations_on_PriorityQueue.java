import java.util.*;

/**
 * Operations_on_PriorityQueue
 */

class Geeks {
    // Function to insert element into the queue
    static void insert(PriorityQueue<Integer> q, int k) {
        q.add(k);
    }

    // Function to find an element k
    static boolean find(PriorityQueue<Integer> q, int k) {
        return q.contains(k);
    }

    // Function to delete the max element from queue
    static int delete(PriorityQueue<Integer> q) {
        int maxel = q.peek();
        while (q.peek() == maxel)
            q.remove(maxel);
        return maxel;
    }
}

public class Operations_on_PriorityQueue {

    public static void main(String[] args) {
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(new Comparator<Integer>() {
            public int compare(Integer w1, Integer w2) {
                return w2.compareTo(w1);
            }
        });

        Geeks gk = new Geeks();
    }
}
