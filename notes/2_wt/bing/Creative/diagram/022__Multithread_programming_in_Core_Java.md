Multithreading in Java is a process of executing multiple threads simultaneously to maximize the utilization of CPU. A thread is a lightweight sub-process, the smallest unit of processing. Multithreading allows concurrent execution of two or more parts of a program  .

There are two ways to create threads in Java: by extending the Thread class or by implementing the Runnable interface. The Thread class provides some built-in methods for thread management, such as start(), run(), sleep(), join(), yield(), interrupt(), etc. The Runnable interface is a functional interface that has only one abstract method: run(). The run() method contains the code that is executed by the thread .

The following diagram illustrates the basic architecture of a multithreaded program in Java:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Main Thread    |       |  Thread 1       |       |  Thread 2       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  run()          |       |  run()          |       |  run()          |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  start()        |       |  start()        |       |  start()        |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Thread class   |       |  Thread class   |       |  Thread class   |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Runnable       |       |  Runnable       |       |  Runnable       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  run()          |       |  run()          |       |  run()          |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Your code      |       |  Your code      |       |  Your code      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The main thread is the first user thread created when the application starts. It can create other threads by instantiating the Thread class and passing a Runnable object to its constructor. The start() method of the Thread class invokes the run() method of the Runnable object, which executes the code defined by the user. The thread scheduler of the operating system is responsible for allocating CPU time to the threads and switching between them .