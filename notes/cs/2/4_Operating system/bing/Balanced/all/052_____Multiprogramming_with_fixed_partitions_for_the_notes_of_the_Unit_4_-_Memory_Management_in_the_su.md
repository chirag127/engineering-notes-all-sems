# Multiprogramming with Fixed Partitions

- Multiprogramming is a technique that allows multiple processes to execute simultaneously in the main memory .
- Multiprogramming with fixed partitions is a contiguous memory management technique in which the main memory is divided into fixed sized partitions which can be of equal or unequal size .
- Each partition can hold one process at a time and the process cannot span across multiple partitions .
- The number of partitions is fixed and determined at system initialization time .
- The partitions can be allocated to processes either statically or dynamically .
  - Static allocation means that each partition is assigned to a specific process class or priority level and the process can only be loaded into its assigned partition .
  - Dynamic allocation means that any free partition that is big enough to hold the process can be allocated to the process .
- The advantages of multiprogramming with fixed partitions are  :
  - It is simple and easy to implement.
  - It avoids external fragmentation as there is no space between partitions.
  - It reduces the overhead of memory management as there is no need to maintain a list of free and allocated blocks.
- The disadvantages of multiprogramming with fixed partitions are  :
  - It suffers from internal fragmentation as the process may not occupy the entire partition and the unused space within the partition is wasted.
  - It limits the degree of multiprogramming as the number of partitions is fixed and may not match the number of processes in the ready queue.
  - It may cause long waiting time and low CPU utilization if the processes are too large or too small for the available partitions.
- Multiprogramming with fixed partitions is different from segmentation in that segmentation allows each process to have multiple non-contiguous segments in the main memory and each segment can have a different size and protection mode. Segmentation also provides logical address space to the process and supports dynamic linking and sharing of code and data.