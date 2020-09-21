import java.util.*;

/**
 * HashMap_4
 */
public class HashMap_4 {
    public static void main(String[] args) {
        Scanner st = new Scanner(System.in);
        
        HashMap<String, Integer> hmap = new HashMap<String, Integer>();
        for (int i = 0; i < st.nextInt(); i++) {

            int valsnum = st.nextInt();
            
            for (int j = 0; j < valsnum; j++)
                hmap.put(st.next(), st.nextInt());
            
            String key = st.next();

            if (hmap.containsKey(key))
                System.out.println(hmap.get(key));
            else
                System.out.println(-1);

            hmap.clear();
        }

        st.close();
    }
}