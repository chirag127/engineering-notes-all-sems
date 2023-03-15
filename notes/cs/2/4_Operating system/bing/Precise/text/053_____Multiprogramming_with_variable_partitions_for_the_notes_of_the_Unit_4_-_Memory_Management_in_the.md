### Multiprogramming with Variable Partitions

- Multiprogramming with variable partitioning is a contiguous memory management technique in which the main memory is not divided into partitions and the process is allocated a chunk of free memory that is big enough for it to fit.
- It is used to alleviate the problem faced by fixed partitioning. As opposed to fixed partitioning, in variable partitioning, partitions are not created until a process executes.
- Implementing variable Partitioning is difficult as compared to Fixed Partitioning as it involves allocation of memory during run-time rather than during system configure.
- There will be external fragmentation inspite of absence of internal fragmentation.
- In multi-programming with fixed partitioning the main memory is divided into fixed sized partitions. In multi-programming with variable partitioning the main memory is not divided into fixed sized partitions.
- Only one process can be placed in a partition.