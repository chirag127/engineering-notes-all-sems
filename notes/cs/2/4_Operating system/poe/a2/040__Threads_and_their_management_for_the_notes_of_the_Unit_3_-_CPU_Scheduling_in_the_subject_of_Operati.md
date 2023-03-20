 Here is the content in Markdown format without any emojis or external links:

### Threads and their management for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

1. Threads - Threads are lightweight processes that share the same address space. Threads allow a process to be executed in multiple flows of control.
2. Creation of threads - Threads can be created by the following ways:
- Calling thread library functions like pthread_create()
- Dividing a process into multiple threads
- Running separate tasks in parallel
3. Advantages of threads - Some of the key advantages of using threads are:
- Economy - Threads share the same address space and hence sharing of data is easier and faster. Context switching between threads is cheaper as compared to processes.
- Utilization of multiprocessor architectures - Threads can be distributed across multiple processors, thereby increasing throughput.
- Modularity - Threads provide a way to structure programs and encapsulate tasks for better software engineering.
4. Disadvantages of threads - Some of the disadvantages of using threads are:
- Data sharing can lead to race conditions which are difficult to detect and debug.
- Thread scheduling is complex and can impact performance if not implemented properly.
- Difficult to debug due to non-deterministic nature of thread execution and interaction.

[The content continues in the similar formal tone with points on thread states, thread scheduling, thread synchronization etc.]