#### Multithread programming in Core Java
Here is an ASCII diagram that illustrates the concept of multithreading in Core Java:

```
 +-------------------+
 |  Thread-1         |
 | +---------------+ |
 | |               | |
 | |  Runnable     | |
 | |               | |
 | +---------------+ |
 +-------------------+
          |
          |
          v
 +-------------------+
 |  Thread-2         |
 | +---------------+ |
 | |               | |
 | |  Runnable     | |
 | |               | |
 | +---------------+ |
 +-------------------+
          |
          |
          v
 +-------------------+
 |  Thread-3         |
 | +---------------+ |
 | |               | |
 | |  Runnable     | |
 | |               | |
 | +---------------+ |
 +-------------------+
```

In this diagram, each box represents a thread, and within each thread is a `Runnable` object. The arrows show the flow of execution between the threads. In a multithreaded program, multiple threads can execute concurrently, allowing for more efficient use of system resources and faster program execution.
