### Thrashing

Thrashing is a condition that occurs when a computer's virtual memory subsystem is in a constant state of paging, rapidly exchanging data in memory for data on disk, to the exclusion of most application-level processing. This causes the performance of the computer to degrade or collapse.

- Thrashing occurs when the system does not have enough memory to support all the running processes.
- When this happens, the operating system starts to continuously swap memory pages between the RAM and the hard disk.
- This constant swapping of memory pages slows down the system significantly, as the hard disk is much slower than the RAM.
- To prevent thrashing, the operating system can use various memory management techniques, such as increasing the amount of physical memory, using more efficient page replacement algorithms, or implementing process scheduling algorithms that reduce the number of processes competing for memory.
- Thrashing can also be reduced by using a technique called working set model, which ensures that only the most recently used memory pages are kept in memory, while the rest are swapped out to disk.