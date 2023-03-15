# Multiprogramming with Fixed Partitions

- Multiprogramming is a technique that allows multiple processes to execute simultaneously in the main memory .
- Multiprogramming with fixed partitions is a contiguous memory management technique in which the main memory is divided into fixed sized partitions which can be of equal or unequal size .
- Each partition can hold one process at a time and the process cannot span across multiple partitions .
- The number and size of the partitions are determined at system initialization and remain fixed throughout the system operation .
- The advantages of multiprogramming with fixed partitions are:
  - It is simple and easy to implement .
  - It avoids external fragmentation as each partition is contiguous .
  - It provides protection and isolation among processes as each process has its own address space and cannot access other processes' partitions.
- The disadvantages of multiprogramming with fixed partitions are:
  - It suffers from internal fragmentation as the process may not fully utilize the allocated partition .
  - It wastes memory space as some partitions may remain unused or underutilized .
  - It limits the degree of multiprogramming as the number of partitions is fixed and cannot be changed dynamically .
  - It may cause long waiting time and low CPU utilization as the processes have to wait for a suitable partition to be available .
  - It does not support dynamic memory allocation and deallocation as the partitions are fixed .
- An example of multiprogramming with fixed partitions is shown below:

![Example of multiprogramming with fixed partitions](https://www.cs.nott.ac.uk/~pszgxk/courses/g53ops/Memory%20Management/images/fixedpartitions.gif)