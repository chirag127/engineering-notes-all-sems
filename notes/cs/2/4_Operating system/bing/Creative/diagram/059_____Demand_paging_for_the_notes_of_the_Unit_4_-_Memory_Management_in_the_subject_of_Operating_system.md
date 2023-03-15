### Demand paging

Demand paging is a method of virtual memory management that allows a process to execute without loading all of its pages into physical memory. It follows that:

- A process begins execution with none of its pages in physical memory, and many page faults will occur until most of a process’s working set of pages are located in physical memory.
- The operating system copies a disk page into physical memory only if an attempt is made to access it and that page is not already in memory (i.e., if a page fault occurs).
- The operating system will page out a page from physical memory to free up space for other pages when necessary.

The advantages of demand paging are:

- It reduces the amount of physical memory needed by a process, as only the pages that are actually used are loaded into memory.
- It allows the execution of processes that are larger than the available physical memory, as the pages can be swapped in and out as needed.
- It improves the performance of the system, as the pages that are not accessed are not wasted in memory.

The disadvantages of demand paging are:

- It increases the overhead of the operating system, as it has to handle page faults, page replacement, and disk I/O.
- It may cause thrashing, which is a situation where the system spends more time swapping pages than executing processes.
- It may degrade the response time of the processes, as they may have to wait for the pages to be loaded from disk.

The main components of demand paging are:

- A page table, which is a data structure that maps the logical addresses of a process to the physical addresses of the pages in memory or disk.
- A valid-invalid bit, which is a flag that indicates whether a page is in memory or not.
- A page fault handler, which is a routine that is invoked when a page fault occurs, and is responsible for finding the required page on disk, allocating a free frame in memory, loading the page into the frame, updating the page table, and resuming the execution of the process.
- A page replacement algorithm, which is a policy that decides which page to evict from memory when a free frame is needed. Some common page replacement algorithms are FIFO, LRU, OPT, etc.