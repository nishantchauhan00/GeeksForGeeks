/*
Thread Synchronization
Synchronization enables you to control program flow and access to shared data 
for concurrently executing threads.

The four synchronization models are mutex locks, read/write locks, condition 
variables, and semaphores.

1. Mutex locks allow only one thread at a time to execute a specific section of 
   code, or to access specific data.

2. Read/write locks permit concurrent reads and exclusive writes to a protected 
   shared resource. To modify a resource, a thread must first acquire the exclusive write lock. An exclusive write lock is not permitted until all read locks have been released.

3. Condition variables block threads until a particular condition is true.

4. Counting semaphores typically coordinate access to resources. The count is 
   the limit on how many threads can have concurrent access to the data protected
   by the semaphore. When the count is reached, the semaphore causes the calling 
   thread to block until the count changes. A binary semaphore (with a count of 
   one) is similar in operation to a mutex lock.


User-Level Threads State
The following state is unique to each thread.
1. Thread ID
2. Register state, including program counter (PC) and stack pointer
3. Stack
4. Signal mask
5. Priority
6. Thread-private storage

*/

#include <iostream>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>

using namespace std;

pthread_mutex_t mutex_lock;

void *printerHello(void *arg){
    
    pthread_mutex_lock(&mutex_lock);

    string name = "hello ";
    name += (char *)arg;
    
    for(char el: name){
        Sleep(100);
        cout<<el;
    }

    cout<<endl;

    pthread_mutex_unlock(&mutex_lock);

    return 0;
}

void *printerBye(void *arg){
    
    pthread_mutex_lock(&mutex_lock);

    string name = "bye ";
    name += (char *)arg;
    
    for(char el: name){
        Sleep(100);
        cout<<el;
    }

    cout<<endl;

    pthread_mutex_unlock(&mutex_lock);

    return 0;
}

int main(int argc, char const *argv[])
{
    pthread_t thread1, thread2;

    pthread_mutex_init(&mutex_lock, nullptr);


    int err1, err2; 
    err1 = pthread_create(&thread1, NULL, printerHello, (void *)argv[1]);
    err2 = pthread_create(&thread2, NULL, printerBye, (void *)argv[1]);

    // order of join in mutex is not affecting
    pthread_join(thread2, nullptr);
    pthread_join(thread1, nullptr);

    if(err1 || err2){
        printf("Error Occurred");
        cout<<err1<<" "<<err2<<endl;
        return 0;
    }
    
    pthread_exit(NULL);

    return EXIT_SUCCESS;
}


