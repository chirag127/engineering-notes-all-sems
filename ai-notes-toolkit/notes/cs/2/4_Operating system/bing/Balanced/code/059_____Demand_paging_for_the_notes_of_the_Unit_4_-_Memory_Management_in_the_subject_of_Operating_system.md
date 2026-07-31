### Demand paging

Demand paging is a memory management scheme used by modern operating systems to manage the limited memory available. It is a method of virtual memory management that allows a process to execute without loading all of its pages into physical memory. Instead, the operating system copies a disk page into physical memory only if an attempt is made to access it and that page is not already in memory (i.e., if a page fault occurs) .

Some of the advantages of demand paging are:

- It reduces the loading time of a process, as only the necessary pages are loaded initially.
- It reduces the memory requirement of a process, as only the pages that are accessed are kept in memory.
- It allows more processes to run concurrently, as the physical memory can be shared among them.
- It allows the use of larger virtual address spaces than the physical memory size.

Some of the challenges of demand paging are:

- It requires a page table to keep track of the mapping between virtual and physical addresses.
- It requires a page replacement algorithm to decide which page to evict when the physical memory is full.
- It requires a page fault handler to handle the page faults and load the missing pages from the disk.
- It increases the disk I/O and CPU overhead, as the pages need to be swapped in and out frequently.

Some of the concepts related to demand paging are:

- Page: A fixed-size block of memory that is the unit of transfer between the disk and the physical memory.
- Frame: A fixed-size block of physical memory that can hold one page.
- Page table: A data structure that stores the mapping between the virtual and physical addresses of each page.
- Page fault: An exception that occurs when a process tries to access a page that is not in memory.
- Page fault handler: A routine that handles the page faults and loads the missing pages from the disk.
- Page replacement algorithm: An algorithm that decides which page to evict from the memory when a new page needs to be loaded.
- Thrashing: A situation where the system spends more time swapping pages than executing processes.