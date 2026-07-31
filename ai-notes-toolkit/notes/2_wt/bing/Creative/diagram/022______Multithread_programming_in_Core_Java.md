Multithread programming in Core Java is a process of executing multiple threads simultaneously to maximize the utilization of CPU. A thread is a lightweight sub-process, the smallest unit of processing. Multithreading allows concurrent execution of two or more parts of a program  .

To create a thread in Java, there are two ways:
- Extending the Thread class and overriding its run() method.
- Implementing the Runnable interface and defining its run() method.

The Thread class provides methods to manage the life cycle of a thread, such as start(), sleep(), join(), interrupt(), etc. The Runnable interface is a functional interface that can be used with lambda expressions .

A thread can be in one of the following states :
- New: The thread is created but not started yet.
- Runnable: The thread is ready to run or running.
- Waiting: The thread is waiting for another thread to perform a task.
- Timed waiting: The thread is waiting for a specified amount of time.
- Blocked: The thread is blocked by a lock or I/O operation.
- Terminated: The thread has completed its execution or stopped by an exception.

The following is a possible ASCII diagram for multithread programming in Core Java:

#### Multithread programming in Core Java

```
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|   Main Thread  |        |   Thread 1     |        |   Thread 2     |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  start()       |------->|  run()         |        |  run()         |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  join()        |<-------|  terminate     |        |  terminate     |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  resume        |        |                |        |                |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
```