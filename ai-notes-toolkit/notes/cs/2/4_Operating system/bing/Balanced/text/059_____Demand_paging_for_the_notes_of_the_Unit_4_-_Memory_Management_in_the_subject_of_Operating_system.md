### Demand paging

- Demand paging is a method of virtual memory management that allows a process to execute without loading all of its pages into physical memory.
- Demand paging works by loading pages from the secondary storage (such as a hard disk) into the main memory only when they are needed or demanded by the CPU.
- Demand paging reduces the amount of physical memory required by a process and allows more processes to run concurrently.
- Demand paging also reduces the I/O overhead and the startup time of a process, as only the necessary pages are loaded initially.
- Demand paging involves the following components and steps:
  - A page table that maps the logical address space of a process to the physical address space of the main memory.
  - A valid-invalid bit for each entry in the page table that indicates whether the corresponding page is in the main memory or not.
  - A page fault handler that is invoked by the operating system when a page fault occurs, i.e., when the CPU tries to access a page that is not in the main memory.
  - A free-frame list that keeps track of the available frames in the main memory.
  - A page replacement algorithm that decides which page to evict from the main memory when there is no free frame available.
  - A fetch policy that determines when a page should be brought into the main memory, either before or after a page fault occurs.
  - A placement policy that determines where a page should be placed in the main memory, either in a fixed or a variable location.
  - A cleaning policy that determines when a modified page should be written back to the secondary storage, either immediately or later.