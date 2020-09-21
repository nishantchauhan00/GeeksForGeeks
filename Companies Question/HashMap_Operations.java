import java.util.HashMap;

/**
 * HashMap_Operations
 */
public class HashMap_Operations {

    /* Inserts an entry with key x and value y in map */
    void add_Value(HashMap<Integer, Integer> hmap, int x, int y) {
        if (hmap.containsKey(x))
            hmap.remove(x);
        
        hmap.put(x, y);
    }

    /* Returns the value with key x from the map */
    int find_value(HashMap<Integer, Integer> hmap, int x) {
        if (hmap.containsKey(x))
            return hmap.get(x);
        else
            return -1;
    }

    /* Returns the size of the map */
    int getSize(HashMap<Integer, Integer> hmap) {
        return hmap.size();
    }

    /* Removes the entry with key x from the map */
    void removeKey(HashMap<Integer, Integer> hmap, int x) {
        hmap.remove(x);
    }

    public static void main(String[] args) {
        HashMap<Integer, Integer> hmap = new HashMap<Integer, Integer>();

    }
}
