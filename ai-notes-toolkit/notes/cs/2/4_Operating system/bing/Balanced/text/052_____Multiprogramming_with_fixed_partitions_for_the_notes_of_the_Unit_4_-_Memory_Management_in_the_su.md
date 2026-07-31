### Multiprogramming with fixed partitions

- Multiprogramming is a technique that allows multiple processes to execute simultaneously in the main memory .
- Fixed partitions are non-overlapping regions of the main memory that have a fixed size and location .
- The number of fixed partitions is determined at system startup and does not change during execution.
- Each partition can hold one process at a time, and the process must fit entirely within the partition .
- The advantages of multiprogramming with fixed partitions are:
  - It is simple and easy to implement .
  - It avoids external fragmentation, as there are no gaps between partitions .
- The disadvantages of multiprogramming with fixed partitions are:
  - It suffers from internal fragmentation, as the unused space within a partition is wasted .
  - It may not utilize the memory efficiently, as some partitions may be too large or too small for some processes .
  - It limits the degree of multiprogramming, as the number of partitions is fixed and may not match the number of ready processes .
  - It requires the processes to be relocatable or position-independent, as they may be loaded into different partitions at different times .