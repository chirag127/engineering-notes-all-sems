### Thrashing

- Thrashing is a phenomenon that occurs when the operating system spends more time swapping pages in and out of the main memory than executing processes.   
- Thrashing happens when the degree of multiprogramming is too high, meaning that too many processes are competing for the limited physical memory.   
- Thrashing reduces the CPU utilization and the system throughput, and causes severe performance problems in the operating system.  
- Thrashing can be detected by monitoring the page fault rate and the CPU utilization. If the page fault rate is high and the CPU utilization is low, then thrashing is likely to occur.  
- Thrashing can be prevented or handled by using various techniques, such as:
  - Working set model: This model keeps track of the pages that a process has accessed recently, and allocates enough frames to each process to hold its working set. If the working set of a process cannot fit in the allocated frames, the process is suspended until more frames are available.  
  - Page fault frequency scheme: This scheme sets upper and lower bounds on the acceptable page fault rate for a process. If the page fault rate of a process is too low, it means that the process has more frames than it needs, and some frames can be taken away. If the page fault rate of a process is too high, it means that the process does not have enough frames, and more frames should be allocated.  
  - Load control: This technique limits the degree of multiprogramming by controlling the number of processes that are in the ready queue. If the system is thrashing, the number of processes should be reduced. If the system is underutilized, the number of processes can be increased.