### Multiprogramming with fixed partitions

- Multiprogramming is a technique that allows multiple processes to execute simultaneously in the main memory.
- Multiprogramming with fixed partitions is a contiguous memory management technique in which the main memory is divided into fixed sized partitions which can be of equal or unequal size   .
- Each partition can hold one process at a time. The number of partitions is fixed and does not change during the execution.
- The operating system maintains a table that keeps track of the status of each partition (free or occupied) and the process assigned to it.
- When a process arrives, the operating system allocates it to a free partition that is big enough to hold the process. If no such partition is available, the process has to wait in the ready queue.
- When a process terminates, the partition becomes free and can be allocated to another process.
- The advantages of multiprogramming with fixed partitions are:
  - It is simple and easy to implement.
  - It avoids external fragmentation as each partition is contiguous.
  - It provides protection and isolation among processes as each process has its own address space and cannot access other processes' partitions.
- The disadvantages of multiprogramming with fixed partitions are:
  - It suffers from internal fragmentation as the allocated partition may be larger than the process size, leaving some unused space within the partition.
  - It has low memory utilization as some partitions may remain unused or underutilized.
  - It has poor flexibility and scalability as the number and size of partitions are fixed and cannot be changed according to the demand.
  - It may cause long waiting time and low throughput as processes have to wait for a suitable partition to be available.

: https://sage-answer.com/what-is-multiprogramming-with-fixed-partition/
: https://gtu-paper-solution.com/Paper-Solution/OperatingSystem-2140702/Winter-2018/3-b-OR
: https://www.geeksforgeeks.org/difference-between-fixed-partitioning-and-variable-partitioning/
: https://www.geeksforgeeks.org/fixed-or-static-partitioning-in-operating-system/
: https://cs.stackexchange.com/questions/76403/how-is-segmentation-different-from-multiprogramming-with-fixed-partition