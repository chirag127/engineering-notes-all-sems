# Performance of Demand Paging

- Demand paging is a memory management technique that allows a process to access pages of its virtual memory on demand, rather than loading them all at once.
- Demand paging can improve the performance of a computer system by reducing the amount of physical memory needed, increasing the degree of multiprogramming, and allowing the execution of programs that are larger than the available memory.
- However, demand paging also introduces some overheads, such as the time required to locate and load a page from the disk, the time required to update the page table and the TLB, and the time required to handle page faults.
- The performance of demand paging can be measured by the effective access time (EAT), which is the average time required to access a page in memory. The EAT depends on the following factors:
  - The memory access time (ma), which is the time required to access a page in memory if it is present.
  - The page fault rate (p), which is the probability that a page is not present in memory and needs to be fetched from the disk.
  - The page fault service time (pf), which is the time required to service a page fault, including the time to locate and load the page from the disk, the time to update the page table and the TLB, and the time to restart the instruction that caused the page fault.
- The EAT can be calculated by the following formula:

  EAT = (1 - p) x ma + p x pf

- The EAT can be reduced by minimizing the page fault rate and the page fault service time. Some techniques to achieve this are:
  - Choosing an appropriate page size that balances the internal and external fragmentation, the number of page table entries, and the disk transfer time.
  - Using a fast disk and a large disk cache to speed up the page loading and writing operations.
  - Using a suitable page replacement algorithm that minimizes the number of page faults and the number of modified pages that need to be written back to the disk.
  - Using a suitable frame allocation policy that distributes the available frames among the processes according to their needs and priorities.
  - Using prefetching and clustering techniques that anticipate the future page requests and load them in advance or in groups.
  - Using copy-on-write and shared memory techniques that avoid unnecessary page duplication and allow multiple processes to access the same pages.