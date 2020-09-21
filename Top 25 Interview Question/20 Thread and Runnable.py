'''
A thread can be defined in two ways. First, by extending a Thread class that 
has already implemented a Runnable interface. Second, by directly implementing 
a Runnable interface. When you define a thread by extending Thread class you 
have to override the run() method in Thread class. When you define a thread 
implementing a Runnable interface you have to implement the only run() method 
of Runnable interface.

One must extend a Thread class only if it has to override or specialise some 
other methods of Thread class. You must implement a Runnable interface if you 
only want to specialise run method only.

Extending the Thread class introduces tight coupling in the code as the code 
of Thread and job of thread is contained by the same class. On the other hand, 
Implementing Runnable interface introduces loose coupling in the code as the 
code of Thread is seprate from the job assigned to the thread.

It is preferred to implement a Runnable interface instead of extending Thread 
class. As implementing Runnable makes your code loosely coupled as the code of 
thread is different from the class that assign job to the thread. It requires 
less memory and also allows a class to inherit any other class.


With implements Runnable:
public class MyRunnable implements Runnable {
    public void run() {
        //Code
    }
}
//Started with a "new Thread(new MyRunnable()).start()" call

Or, with extends Thread:
public class MyThread extends Thread {
    public MyThread() {
        super("MyThread");
    }
    public void run() {
        //Code
    }
}
//Started with a "new MyThread().start()" call


THREAD	
Basic:	Each thread creates a unique object and gets associated with it.	
Memory:	As each thread create a unique object, more memory required.	

RUNNABLE
Multiple threads share the same objects.
As multiple threads share the same object less memory is used.


In general, I would recommend using something like Runnable rather than Thread 
because it allows you to keep your work only loosely coupled with your choice 
of concurrency. For example, if you use a Runnable and decide later on that 
this doesn't in fact require it's own Thread, you can just call threadA.run().

'''


