### Multiprogramming with fixed partitions

- Multiprogramming is a technique that allows multiple processes to execute simultaneously in the main memory .
- Multiprogramming with fixed partitions is a contiguous memory management technique in which the main memory is divided into fixed sized partitions which can be of equal or unequal size .
- Each partition can hold one process at a time and the process cannot span across multiple partitions .
- The number of partitions is fixed and determined at system initialization time .
- The partitions can be allocated to processes either statically or dynamically .
- Static allocation means that each partition is assigned to a specific process or a class of processes (such as system or user) and cannot be changed .
- Dynamic allocation means that each partition is assigned to any process that requests it and can be changed as processes enter and exit the system .
- The advantages of multiprogramming with fixed partitions are  :
  - It is simple and easy to implement.
  - It avoids external fragmentation as each partition is contiguous.
  - It provides protection and isolation between processes as they cannot access each other's partitions.
- The disadvantages of multiprogramming with fixed partitions are  :
  - It suffers from internal fragmentation as the partition size may not match the process size exactly.
  - It wastes memory space as some partitions may remain unused or underutilized.
  - It limits the degree of multiprogramming as the number of partitions is fixed and may not accommodate all the processes in the ready queue.
  - It may cause long waiting time and low CPU utilization as processes have to wait for a suitable partition to become available.