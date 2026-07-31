#### Multithread programming in Core Java
Multithreading is a feature of Java that allows multiple threads of execution to run concurrently within a single program. A thread is a lightweight sub-process that can perform a specific task. Threads can share the same memory space and resources of the program, but have their own stack, program counter, and local variables. Multithreading can improve the performance and responsiveness of a program by utilizing the available CPU cores and parallelizing the tasks.

To create a thread in Java, there are two ways:

- Extending the `Thread` class and overriding its `run()` method. The `run()` method contains the logic of the thread. To start the thread, an object of the subclass is created and its `start()` method is invoked. The `start()` method internally calls the `run()` method of the thread.

- Implementing the `Runnable` interface and providing an implementation for its `run()` method. The `Runnable` object is then passed to the constructor of the `Thread` class, which creates a new thread. The `start()` method of the `Thread` object is then invoked to start the thread.

Here is an example of both ways:

```java
// Extending the Thread class
class MyThread extends Thread {
  public void run() {
    System.out.println("Hello from MyThread");
  }
}

// Implementing the Runnable interface
class MyRunnable implements Runnable {
  public void run() {
    System.out.println("Hello from MyRunnable");
  }
}

public class Main {
  public static void main(String[] args) {
    // Creating and starting a thread using the Thread class
    MyThread t1 = new MyThread();
    t1.start();

    // Creating and starting a thread using the Runnable interface
    MyRunnable r1 = new MyRunnable();
    Thread t2 = new Thread(r1);
    t2.start();
  }
}
```

The output of the program may vary depending on the order of execution of the threads, but it will print something like:

```
Hello from MyThread
Hello from MyRunnable
```

Some of the methods and properties of the `Thread` class are:

- `getName()` and `setName(String name)` - get and set the name of the thread
- `getPriority()` and `setPriority(int priority)` - get and set the priority of the thread, which affects the scheduling of the thread by the operating system. The priority ranges from 1 (lowest) to 10 (highest), and the default is 5.
- `isAlive()` - check if the thread is still running
- `join()` - wait for the thread to finish its execution
- `sleep(long millis)` - make the thread pause its execution for a specified amount of milliseconds
- `yield()` - make the thread give up its current CPU time slice and allow other threads to run
- `interrupt()` - send an interrupt signal to the thread, which may cause it to stop its execution if it is waiting or sleeping
- `isInterrupted()` and `interrupted()` - check if the thread has been interrupted
- `currentThread()` - get a reference to the currently executing thread
- `getId()` - get the unique identifier of the thread
- `getState()` - get the current state of the thread, which can be one of the following: `NEW`, `RUNNABLE`, `BLOCKED`, `WAITING`, `TIMED_WAITING`, or `TERMINATED`