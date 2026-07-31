# Performance of Demand Paging

- Demand paging is a memory management technique that allows a process to access its virtual memory pages only when they are needed, rather than loading them all into physical memory at once.
- Demand paging can improve the memory utilization and reduce the I/O overhead, but it also introduces the possibility of page faults, which occur when a process tries to access a page that is not in physical memory.
- Page faults require the operating system to find a free frame in physical memory, swap out the page that occupies it (if any), load the requested page from the disk, update the page table, and resume the process execution.
- The performance of demand paging depends on the probability of page faults, the memory access time, and the page fault service time.
- The effective access time (EAT) is the average time required to access a page in memory, taking into account the possibility of page faults. It can be calculated as:

  EAT = (1 - p) x ma + p x pf

  where p is the probability of a page fault, ma is the memory access time, and pf is the page fault service time.

- The page fault service time consists of several components, such as:

  - The time to interrupt the process and switch to the operating system.
  - The time to search the page table and the disk directory to find the location of the page on the disk.
  - The time to schedule the disk I/O request and wait for the disk to rotate and seek the page.
  - The time to transfer the page from the disk to the memory.
  - The time to update the page table and the frame table.
  - The time to restart the process and resume its execution.

- The page fault service time is typically much larger than the memory access time, so the performance of demand paging is highly sensitive to the page fault rate. A low page fault rate can result in an acceptable EAT, while a high page fault rate can degrade the performance significantly.
- The page fault rate can be influenced by several factors, such as:

  - The page size: Larger pages can reduce the number of page faults, but they also increase the internal fragmentation and the disk transfer time.
  - The degree of multiprogramming: Higher degree of multiprogramming can increase the memory utilization and the CPU utilization, but it also increases the competition for physical frames and the page fault rate.
  - The replacement algorithm: The replacement algorithm determines which page to swap out when a page fault occurs. A good replacement algorithm can minimize the number of page faults by choosing the page that is least likely to be used in the near future.
  - The allocation policy: The allocation policy determines how many frames to allocate to each process. A fair allocation policy can balance the memory needs of different processes and avoid thrashing, which is a situation where the system spends more time swapping pages than executing processes.