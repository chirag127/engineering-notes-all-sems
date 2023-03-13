#### Multithread programming in Core Java

- Multithread programming in Core Java is a process of executing two or more threads simultaneously to maximize the utilization of CPU  .
- A thread is a lightweight sub-process, the smallest unit of processing. Threads are independent paths of execution within a process.
- Multithreading allows concurrent execution of two or more parts of a program, which can improve the performance and responsiveness of the application .
- Multithreading can also help to achieve multitasking, which is the ability of a system to perform multiple tasks at the same time.
- Multithreading can be implemented in Java by using two mechanisms: extending the Thread class or implementing the Runnable interface .
- The Thread class provides methods to create and manage threads, such as start(), run(), sleep(), join(), interrupt(), etc .
- The Runnable interface defines a single method, run(), that contains the code to be executed by the thread .
- A thread can have one of the following states: new, runnable, running, waiting, timed waiting, blocked, or terminated .
- A thread can communicate with other threads by using methods such as wait(), notify(), and notifyAll(), which are defined in the Object class .
- A thread can also synchronize its access to shared resources by using the synchronized keyword or the Lock interface .
- Some of the advantages of multithreading are: increased throughput, improved CPU utilization, better resource management, and enhanced user experience .
- Some of the disadvantages of multithreading are: increased complexity, increased overhead, potential deadlock, and concurrency issues .

Here is an example of creating and running two threads in Java by extending the Thread class:

```java
// A class that extends the Thread class
class MyThread extends Thread {
  // A constructor that takes a name for the thread
  public MyThread(String name) {
    super(name); // Call the super class constructor
  }

  // The run method that contains the code to be executed by the thread
  public void run() {
    // Print the name of the thread and a message
    System.out.println("Hello from " + getName());
  }
}

// A class that contains the main method
class Main {
  // The main method
  public static void main(String[] args) {
    // Create two instances of MyThread with different names
    MyThread t1 = new MyThread("Thread 1");
    MyThread t2 = new MyThread("Thread 2");

    // Start the threads
    t1.start();
    t2.start();
  }
}
```

The output of the program may vary depending on the order of execution of the threads, but it could be something like this:

```
Hello from Thread 1
Hello from Thread 2
```

Here is an example of creating and running two threads in Java by implementing the Runnable interface:

```java
// A class that implements the Runnable interface
class MyRunnable implements Runnable {
  // A constructor that takes a name for the thread
  public MyRunnable(String name) {
    // Create a new Thread object with this Runnable and the name
    Thread t = new Thread(this, name);
    // Start the thread
    t.start();
  }

  // The run method that contains the code to be executed by the thread
  public void run() {
    // Print the name of the thread and a message
    System.out.println("Hello from " + Thread.currentThread().getName());
  }
}

// A class that contains the main method
class Main {
  // The main method
  public static void main(String[] args) {
    // Create two instances of MyRunnable with different names
    MyRunnable r1 = new MyRunnable("Thread 1");
    MyRunnable r2 = new MyRunnable("Thread 2");
  }
}
```

The output of the program may vary depending on the order of execution of the threads, but it could be something like this:

```
Hello from Thread 1
Hello from Thread 2
```

Here is a possible mnemonic to remember the thread states in Java:

**N**ew **R**unners **R**un **W**ithout **T**iming