#### Multithread programming in Core Java

Multithreading is a feature of Java that allows multiple threads of execution to run concurrently within a single program. A thread is a lightweight sub-process that can perform a specific task. Threads can share the same memory space and resources of the program, but have their own stack, program counter and local variables. Multithreading can improve the performance and responsiveness of a program by utilizing the available CPU cores and parallelizing the tasks.

To create a thread in Java, there are two ways:

- Extending the `Thread` class and overriding its `run()` method. The `run()` method contains the code that the thread will execute. To start the thread, an object of the subclass must be created and its `start()` method must be invoked.
- Implementing the `Runnable` interface and providing an implementation for its `run()` method. The `run()` method contains the code that the thread will execute. To start the thread, an object of the class that implements `Runnable` must be passed to the constructor of the `Thread` class and its `start()` method must be invoked.

Here is an example of creating two threads using both ways:

```java
// A class that extends Thread
class MyThread extends Thread {
  // The run() method that will be executed by the thread
  public void run() {
    System.out.println("Hello from MyThread");
  }
}

// A class that implements Runnable
class MyRunnable implements Runnable {
  // The run() method that will be executed by the thread
  public void run() {
    System.out.println("Hello from MyRunnable");
  }
}

// The main class
public class Main {
  public static void main(String[] args) {
    // Creating and starting a thread using MyThread
    MyThread t1 = new MyThread();
    t1.start();

    // Creating and starting a thread using MyRunnable
    MyRunnable r1 = new MyRunnable();
    Thread t2 = new Thread(r1);
    t2.start();
  }
}
```

The output of the program may vary depending on the order of execution of the threads, but it will look something like this:

```
Hello from MyThread
Hello from MyRunnable
```