#### Multithread programming in Core Java

- Multithread programming in Core Java is a process of executing two or more threads simultaneously to maximize the utilization of CPU  .
- A thread is a lightweight sub-process, the smallest unit of processing. Threads can share the same memory space and resources of the process they belong to.
- Multithreading can improve the performance and responsiveness of an application by allowing it to perform multiple tasks concurrently  .
- Multithreading can also reduce the idle time of CPU by switching between threads that are ready to run.
- Multithreading can be achieved in Java by two ways:
  - Extending the `Thread` class and overriding its `run()` method.
  - Implementing the `Runnable` interface and providing its `run()` method.
- The `run()` method contains the logic of the thread and is invoked by the `start()` method of the `Thread` class .
- The `Thread` class also provides methods to control the behavior and state of the threads, such as `sleep()`, `join()`, `wait()`, `notify()`, `notifyAll()`, etc .
- The `Thread` class also has a static method `currentThread()` that returns the reference of the currently executing thread.
- The `Thread` class also has a field `priority` that determines the order of execution of the threads by the thread scheduler.
- The thread scheduler is a part of the JVM that decides which thread should run at a given time .
- The thread scheduler uses a preemptive or time-slicing algorithm to allocate CPU time to the threads .
- The thread scheduler can also take into account the number of cores available in the system and run multiple threads simultaneously on different cores.
- Multithreading can have some challenges and drawbacks, such as  :
  - Thread synchronization: The need to coordinate the access and modification of shared resources by multiple threads to avoid data inconsistency and deadlock.
  - Thread communication: The need to exchange information and signals between threads to coordinate their actions and states.
  - Thread management: The need to create, start, stop, and destroy threads efficiently and safely.
  - Thread overhead: The extra memory and CPU time required to create and maintain threads and their context switching.

- A possible mnemonic to remember the benefits of multithreading is **PARIS**:
  - **P**erformance: Multithreading can improve the performance of an application by utilizing the CPU resources better.
  - **A**synchronous: Multithreading can allow an application to perform multiple tasks asynchronously without blocking the main thread.
  - **R**esponsiveness: Multithreading can improve the responsiveness of an application by allowing it to handle user inputs and events while performing background tasks.
  - **I**dle time: Multithreading can reduce the idle time of CPU by switching between threads that are ready to run.
  - **S**calability: Multithreading can make an application more scalable by taking advantage of the multiple cores available in the system.

: Multithreading in Java Tutorial with Program & Examples - Guru99
: Multithreading in Java - GeeksforGeeks
: Multithreading in Java - javatpoint
: Multithreading in Java - Everything You MUST Know | DigitalOcean
: Multithreading in Java: How to Get Started with Threads - freeCodeCamp.org
: This is a self-generated mnemonic based on the information from the search results.