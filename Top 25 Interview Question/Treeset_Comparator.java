import java.util.*;

// Comparators in TreeSet
/*
The java.util.TreeSet.comparator() method shares an important function of 
setting and returning the comparator that can be used to order the elements in 
a TreeSet. The method returns Null value if the set follows the natural ordering 
pattern of the elements.

Syntax:
comp_set = (TreeSet)tree_set.comparator()
 */



class NumComparator implements Comparator<Integer> {
    @Override
    public int compare(Integer num1, Integer num2) 
    { 
        return num1-num2; 
    } 
}

public class Treeset_Comparator {
    public static void main(String[] args) {
        TreeSet<Integer> tset = new TreeSet<Integer>(new NumComparator());

        for(int i=0; i<5; i++)
            tset.add(i+1);
        
        System.out.println(tset);
            
        tset.add(5);
            
        System.out.println(tset);
        
        System.out.println(tset.comparator());

    }
}

