### Principle of Concurrency

- Concurrency in operating system refers to the execution of multiple instruction sequences at the same time   .
- It occurs when there are several process threads running in parallel   .
- These threads can interact with each other through shared memory or message passing .
- Concurrency provides an impression of a synchronous computation .
- Concurrency can be achieved by using current technology such as multi-core processors and parallel processing.
- Some of the principles of concurrency are:
  - Mutual exclusion: It ensures that only one thread can access a shared resource at a time.
  - Synchronization: It coordinates the execution of threads that depend on each other or on a shared resource.
  - Deadlock: It is a situation where two or more threads are waiting for each other to release a resource, resulting in a circular wait.
  - Starvation: It is a situation where a thread is unable to access a resource for a long time due to the interference of other threads.
  - Livelock: It is a situation where two or more threads are constantly changing their state in response to each other, without making any progress.
- Some of the advantages of concurrency are:
  - Improved performance: It allows the system to utilize the available resources more efficiently and execute multiple tasks faster.
  - Improved responsiveness: It allows the system to respond to user requests or external events more quickly and smoothly.
  - Improved modularity: It allows the system to divide a complex problem into smaller and independent subtasks that can be executed concurrently.
  - Improved scalability: It allows the system to handle an increased workload or demand by adding more resources or processors.