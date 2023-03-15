### Thrashing
Thrashing is a condition that occurs when a computer's virtual memory subsystem is in a constant state of paging, rapidly exchanging data in memory for data on disk, to the exclusion of most application-level processing. This causes the performance of the computer to degrade or collapse.

Here are some key points to remember about thrashing:
- Thrashing occurs when the system spends more time paging than executing user programs.
- It is caused by an excessive number of page faults.
- It can be a result of the system having insufficient memory to meet the demands of all running processes.
- To prevent thrashing, the system can use various memory management techniques such as increasing the amount of physical memory, implementing a more efficient page replacement algorithm, or reducing the number of running processes.
- Thrashing can also be reduced by using a technique called working set model, which keeps track of the most recently used pages and ensures that they are kept in memory.
- Another technique to reduce thrashing is the use of a local page replacement policy, where each process is allocated a fixed number of frames and is responsible for managing its own page replacement.
