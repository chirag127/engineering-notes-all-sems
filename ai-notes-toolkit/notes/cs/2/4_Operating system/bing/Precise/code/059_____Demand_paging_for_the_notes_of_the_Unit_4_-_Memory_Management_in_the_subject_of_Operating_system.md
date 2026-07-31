### Demand Paging

Demand paging is a memory management technique used by operating systems to load pages into memory only when they are needed. This technique is used to reduce the amount of physical memory required by a program, as well as to reduce the time it takes to start the program.

Here are some key points to remember about demand paging:

1. **Virtual Memory:** Demand paging is used in conjunction with virtual memory, which allows programs to use more memory than is physically available by temporarily moving pages of data from RAM to disk storage.

2. **Page Faults:** When a program tries to access a page that is not currently in memory, a page fault occurs. The operating system then loads the required page from disk into memory.

3. **Swapping:** The operating system may need to swap out pages from memory to disk in order to make room for new pages. This process is known as swapping.

4. **Page Replacement Algorithms:** The operating system uses page replacement algorithms to determine which pages should be swapped out of memory. Some common algorithms include the Least Recently Used (LRU) and the First-In, First-Out (FIFO) algorithms.

5. **Performance:** Demand paging can improve the performance of a system by reducing the amount of physical memory required by programs. However, if the system does not have enough memory or if the page replacement algorithms are not effective, demand paging can cause thrashing, which can significantly reduce performance.

6. **Implementation:** Demand paging is implemented by the operating system's memory manager. The memory manager is responsible for handling page faults, swapping pages, and managing the allocation of memory to programs.
