Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of multiprocessor scheduling for the unit 3 of CPU scheduling in the subject of operating system.

### Multiprocessor Scheduling

- Multiprocessor scheduling is the process of allocating processes or threads to multiple processors in a system that has more than one processor but shares the same memory, bus, and input/output devices  .
- The main objectives of multiprocessor scheduling are to achieve high performance, high throughput, high utilization, load balancing, and fairness .
- There are two main approaches to multiprocessor scheduling: symmetric multiprocessing and asymmetric multiprocessing .
  - Symmetric multiprocessing (SMP) is where each processor is self-scheduling and can run any process or thread in the system. All processes may be in a common ready queue, or each processor may have its own private queue for ready processes .
  - Asymmetric multiprocessing (AMP) is where one processor is designated as the master processor and is responsible for scheduling processes or threads to the other processors, which are called slave processors. The master processor may also run processes or threads, or it may be dedicated to scheduling only .
- There are different types of multiprocessor scheduling algorithms, such as static partitioning, dynamic partitioning, global queue, distributed queue, and gang scheduling  .
  - Static partitioning is where the processes or threads are assigned to processors at compile time or load time, and the assignment does not change during execution. This approach is simple and avoids overhead, but it may lead to poor load balancing and low utilization .
  - Dynamic partitioning is where the processes or threads are assigned to processors at run time, and the assignment may change during execution. This approach is more flexible and can adapt to the workload, but it may incur overhead and complexity .
  - Global queue is where all the processes or threads are in a single ready queue, and any processor can pick a process or thread from the queue. This approach is easy to implement and can achieve load balancing, but it may cause contention and synchronization issues .
  - Distributed queue is where each processor has its own ready queue, and processes or threads are distributed among the queues. This approach can reduce contention and synchronization issues, but it may cause load imbalance and migration overhead .
  - Gang scheduling is where a group of related processes or threads, called a gang, are scheduled together on a set of processors, and the processors are synchronized to execute the gang in parallel. This approach can improve performance and communication, but it may waste resources and require coordination .
