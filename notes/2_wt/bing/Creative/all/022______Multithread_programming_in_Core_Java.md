#### Multithread programming in Core Java

- Multithread programming in Core Java is a process of executing two or more threads simultaneously to maximum utilization of CPU  .
- A thread is a lightweight sub-process, the smallest unit of processing. Threads are independent and can run concurrently within a process.
- Multithreaded applications can perform multiple tasks at the same time, such as downloading files, playing music, updating user interface, etc .
- Multithreading can improve the performance, responsiveness, and scalability of an application .
- Multithreading can also introduce some challenges, such as synchronization, deadlock, race condition, memory management, etc .

- There are two ways to create a thread in Java :
  - Extending the `Thread` class and overriding its `run()` method.
  - Implementing the `Runnable` interface and defining its `run()` method.
- The `run()` method contains the logic of the thread and is invoked by the `start()` method of the `Thread` class .
- The `start()` method creates a new thread and registers it with the thread scheduler, which decides when to run the thread .
- The thread scheduler can switch between threads based on their priority, state, and availability of CPU cores .
- The thread states are: `NEW`, `RUNNABLE`, `BLOCKED`, `WAITING`, `TIMED_WAITING`, and `TERMINATED` .
- The thread can change its state by using methods such as `sleep()`, `join()`, `wait()`, `notify()`, `notifyAll()`, etc .
- The thread can also communicate with other threads by using shared variables, locks, monitors, semaphores, etc .

- A possible mnemonic to remember the thread states is: **N**ever **R**un **B**efore **W**arming **T**horoughly, **T**hen **E**nd.
- A possible learning trick to understand the difference between `Thread` and `Runnable` is: **T**hread **I**s **A** **T**hread, **R**unnable **H**as **A** **T**hread.
- A possible example of multithreading in Java is:

```java
// A class that implements Runnable interface
class MyRunnable implements Runnable {
  // The run method that contains the thread logic
  public void run() {
    System.out.println("Hello from " + Thread.currentThread().getName());
  }
}

// The main class that creates and starts threads
public class Main {
  public static void main(String[] args) {
    // Creating two objects of MyRunnable class
    MyRunnable r1 = new MyRunnable();
    MyRunnable r2 = new MyRunnable();

    // Creating two threads with the runnable objects
    Thread t1 = new Thread(r1, "Thread-1");
    Thread t2 = new Thread(r2, "Thread-2");

    // Starting the threads
    t1.start();
    t2.start();
  }
}
```

- The possible output of the above program is:

```
Hello from Thread-1
Hello from Thread-2
```

- The order of the output may vary depending on the thread scheduler.