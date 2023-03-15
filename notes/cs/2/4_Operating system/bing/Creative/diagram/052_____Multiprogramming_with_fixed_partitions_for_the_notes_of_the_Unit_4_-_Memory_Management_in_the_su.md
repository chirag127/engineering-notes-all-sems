### Multiprogramming with fixed partitions

- Multiprogramming is a technique that allows multiple processes to execute simultaneously in the main memory .
- Fixed partitions are non-overlapping regions of the main memory that have a fixed size and location .
- The number of partitions is determined at system startup and does not change during execution .
- The size of each partition can be equal or unequal, depending on the system design   .
- Each partition can hold only one process at a time, and the process must fit entirely within the partition .
- A process can be allocated to any free partition that is large enough to accommodate it   .
- The process has complete access to its own address space and no access to any other process's address space.
- The process may or may not be aware of the position of its address space in the physical memory.
- The process can make system calls to request services from the operating system.
- The advantages of multiprogramming with fixed partitions are:
  - It is simple and easy to implement .
  - It provides protection and isolation among processes  .
  - It reduces external fragmentation, as there are no gaps between partitions .
- The disadvantages of multiprogramming with fixed partitions are:
  - It causes internal fragmentation, as the allocated partition may be larger than the process size .
  - It limits the degree of multiprogramming, as the number of partitions is fixed .
  - It wastes memory space, as some partitions may remain unused or underutilized .
  - It may lead to long waiting times, as processes have to wait for a suitable partition to become available .
- An example of multiprogramming with fixed partitions is shown in the following diagram:

| Partition 1 | Partition 2 | Partition 3 | Partition 4 |
|-------------|-------------|-------------|-------------|
| Process A   | Process B   | Process C   | Process D   |
| 64 KB       | 32 KB       | 16 KB       | 8 KB        |