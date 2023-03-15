### Multiprogramming with fixed partitions

- Multiprogramming is a technique that allows multiple processes to execute simultaneously in the main memory .
- Fixed partitions are non-overlapping regions of memory that are allocated to processes at the time of loading.
- The number and size of partitions can be equal or unequal, depending on the system design   .
- The advantages of multiprogramming with fixed partitions are:
  - It is simple and easy to implement.
  - It avoids external fragmentation, as each partition has a fixed size.
  - It provides protection and isolation between processes, as each process has its own address space.
- The disadvantages of multiprogramming with fixed partitions are:
  - It suffers from internal fragmentation, as the allocated partition may be larger than the process size .
  - It wastes memory space, as some partitions may remain unused or underutilized .
  - It limits the degree of multiprogramming, as the number of partitions is fixed.
  - It requires relocation and mapping of logical addresses to physical addresses .