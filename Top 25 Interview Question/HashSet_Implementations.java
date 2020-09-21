import java.util.HashSet;

// Few important features of HashSet are:
// > Implements Set Interface.
// > Underlying data structure for HashSet is hashtable.
// > As it implements the Set Interface, duplicate values are not allowed.
// > Objects that you insert in HashSet are not guaranteed to be inserted in same 
//   order. Objects are inserted based on their hash code.
// > NULL elements are allowed in HashSet.
// > HashSet also implements Searlizable and Cloneable interfaces.


// public class HashSet<E>
//     extends AbstractSet<E>
//     implements Set<E>, Cloneable, java.io.Serializable

public class HashSet_Implementations {
    public static void main(String[] args) {
        HashSet<Integer> sHashSet = new HashSet<Integer>();
        
        for (int i = 0; i<3; i++)
            sHashSet.add(i+1);

        for(Integer x: sHashSet)
            System.out.print(x);

        sHashSet.remove(2); 
        sHashSet.add(3); 
        sHashSet.add(4); 
        
        System.out.println("\n" + sHashSet.hashCode());
        System.out.println(sHashSet.toString());

        for(Integer x: sHashSet)
            System.out.print(x);
    }
}
