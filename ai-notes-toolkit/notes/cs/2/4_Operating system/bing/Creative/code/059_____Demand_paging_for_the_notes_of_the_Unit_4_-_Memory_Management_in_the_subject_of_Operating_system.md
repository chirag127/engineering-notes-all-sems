# Demand paging

Demand paging is a memory management scheme used by modern operating systems to manage the limited memory available. It is a method of virtual memory management that allows a process to execute without loading all of its pages into physical memory at once. Instead, the operating system copies a disk page into physical memory only if an attempt is made to access it and that page is not already in memory (i.e., if a page fault occurs) .

Some of the advantages of demand paging are:

- It reduces the amount of physical memory needed by a process, as only the pages that are actually used are loaded.
- It allows more processes to run concurrently, as the total memory requirement of all processes can exceed the physical memory available.
- It improves the response time of a process, as it can start execution without waiting for all of its pages to be loaded.
- It reduces the disk I/O overhead, as only the pages that are needed are read from the disk.

Some of the challenges of demand paging are:

- It requires a page table to keep track of the mapping between virtual and physical addresses of pages.
- It requires a page replacement algorithm to decide which page to evict from the physical memory when a new page is needed.
- It increases the CPU overhead, as a page fault handler has to be invoked every time a page fault occurs.
- It may cause thrashing, which is a situation where a process spends more time swapping pages than executing. This can happen if the working set of a process (the set of pages that are frequently accessed) is larger than the available physical memory.