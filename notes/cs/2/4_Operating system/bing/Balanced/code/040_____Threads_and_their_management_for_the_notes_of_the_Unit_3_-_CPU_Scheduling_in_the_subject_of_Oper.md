### Threads and their management

- A thread is a single sequence stream within a process. It is a lightweight process that the operating system can schedule and run concurrently with other threads.
- Threads share the same data and code as the process that created them, so they have low operational cost and fast communication.
- Threads can be used to improve the performance, responsiveness, and resource utilization of a system.
- There are two major types of threads in operating systems: user threads and kernel threads .
  - User threads are created and managed by user-level libraries, such as POSIX threads (pthreads) or Java threads. They are not visible to the kernel and do not require system calls to switch between them .
  - Kernel threads are created and managed by the kernel, and can use system calls and access kernel resources. They are visible to the user and can be mapped to one or more user threads .
- There are different ways of mapping user threads to kernel threads, such as one-to-one, many-to-one, many-to-many, or hybrid.
  - One-to-one mapping assigns one user thread to one kernel thread, allowing concurrency and parallelism, but also increasing the overhead of creating and managing kernel threads.
  - Many-to-one mapping assigns many user threads to one kernel thread, reducing the overhead of kernel threads, but also limiting concurrency and parallelism, and blocking the entire process if one user thread makes a blocking system call.
  - Many-to-many mapping assigns many user threads to a pool of kernel threads, allowing concurrency and parallelism, and avoiding blocking the entire process, but also increasing the complexity of scheduling and synchronization.
  - Hybrid mapping combines many-to-many mapping with one-to-one mapping, allowing the creation of additional kernel threads when a user thread makes a blocking system call.
- Threads can be managed by the operating system using various policies and algorithms, such as thread scheduling, thread synchronization, thread communication, and thread termination.
  - Thread scheduling determines which thread should run next on the CPU, based on factors such as priority, fairness, and responsiveness.
  - Thread synchronization ensures that threads access shared resources in a consistent and orderly manner, using mechanisms such as locks, semaphores, monitors, and condition variables.
  - Thread communication allows threads to exchange information and coordinate their actions, using methods such as message passing, shared memory, signals, and pipes.
  - Thread termination occurs when a thread completes its execution, either voluntarily or involuntarily, and releases its resources.