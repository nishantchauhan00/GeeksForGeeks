/**
 * https://javarevisited.blogspot.com/2014/05/double-checked-locking-on-singleton-in-java.html
 * 
 * In object-oriented programming, a singleton class is a class that can have
 * only one object (an instance of the class) at a time. After first time, if we
 * try to instantiate the Singleton class, the new variable also points to the
 * first instance created. So whatever modifications we do to any variable
 * inside the class through any instance, it affects the variable of the single
 * instance created and is visible if we access that variable through any
 * variable of that class type defined.
 * 
 * To design a singleton class: > Make constructor as private. > Write a static
 * method that has return type object of this singleton class. Here, the concept
 * of Lazy initialization is used to write this static method. > Normal class vs
 * Singleton class: Difference in normal and singleton class in terms of
 * instantiation is that, For normal class we use constructor, whereas for
 * singleton class we use getInstance() method. In general, to avoid confusion
 * we may also use the class name as method name while defining this method.
 * 
 * 
 * Double_checking_Singleton
 */

/*
 * this wont work for multithread, for it we can make method 'synchronized' or
 * use Double_checking_Singleton Though synchronized is a thread-safe and solves
 * issue of multiple instance, it's not very efficient. You need to bear cost of
 * synchronization all the time you call this method, while synchronization is
 * only needed on first class, when Singleton instance is created.
 * 
 */
class Singleton {
    // https://www.geeksforgeeks.org/singleton-class-java/

    // static variable single_instance of type Singleton
    private static Singleton single_instance = null;

    // variable of type String
    public String s;

    // private constructor restricted to this class itself
    private Singleton(String ss) {
        s = ss;
        System.out.println("single Instance");
    }

    // static method to create instance of Singleton class
    public static Singleton getInstance(String ss) {
        if (single_instance == null)
            single_instance = new Singleton(ss); // lazy initialization
        return single_instance;
    }
}

class Singleton_DA { // singleton with double checking
    // static variable single_instance of type Singleton
    // the volatile keyword in Java is used as an indicator to Java compiler and
    // Thread that do not cache the value of this variable and always read it 
    // from the main memory.
    private volatile static Singleton_DA single_instance = null;

    // variable of type String
    public String s;

    // private constructor restricted to this class itself
    private Singleton_DA(String ss) {
        s = ss;
        System.out.println("single Instance");
    }

    /**
     * @return Singleton_DA instance
     *         the single_instance Double checked locking pattern, where only
     *         critical section of code is locked. Programmer call it double checked
     *         locking because there are two checks for _instance == null, one
     *         without locking and other with locking (inside synchronized) block.
     */
    public static Singleton_DA getSingle_instance(String ss) {
        if (single_instance == null) {                  // Single Checked
            synchronized (Singleton.class) {
                if (single_instance == null) {          // Double Checked
                    single_instance = new Singleton_DA(ss);
                }
            }
        }
        return single_instance;
    }
}

public class Double_checking_Singleton {

    public static void main(String[] args) {
        /*
        Singleton s1 = Singleton.getInstance("as");
        Singleton s2 = Singleton.getInstance("ass");
        Singleton s3 = Singleton.getInstance("asss");

        s1.s = (s1.s).toLowerCase();
        System.out.println(s1.s);
        System.out.println(s2.s);
        System.out.println(s3.s);

        s3.s = (s3.s).toUpperCase();
        System.out.println(s1.s);
        System.out.println(s2.s);
        System.out.println(s3.s);
        // prints-
        // single Instance
        // as
        // as
        // as
        // AS
        // AS
        // AS
        */

        Singleton_DA s1 = Singleton_DA.getSingle_instance("as");
        Singleton_DA s2 = Singleton_DA.getSingle_instance("ass");
        Singleton_DA s3 = Singleton_DA.getSingle_instance("asss");

        s1.s = (s1.s).toLowerCase();
        System.out.println(s1.s);
        System.out.println(s2.s);
        System.out.println(s3.s);

        s3.s = (s3.s).toUpperCase();
        System.out.println(s1.s);
        System.out.println(s2.s);
        System.out.println(s3.s);
        // prints-
        // single Instance
        // as
        // as
        // as
        // AS
        // AS
        // AS
    }
}

// javac -d exe Double_checking_Singleton.java
// java -cp exe Double_checking_Singleton
