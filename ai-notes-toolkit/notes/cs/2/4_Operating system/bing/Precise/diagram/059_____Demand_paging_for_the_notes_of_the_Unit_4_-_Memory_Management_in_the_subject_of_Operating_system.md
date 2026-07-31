### Demand Paging

Demand paging is a memory management technique used in operating systems where pages are brought into memory only when they are needed. This is in contrast to pre-paging, where pages are loaded into memory before they are needed.

Here are some key points to remember about demand paging:

1. Demand paging is used to reduce the amount of physical memory required by a program.
2. Pages are brought into memory only when they are needed, which can reduce the amount of time it takes to start a program.
3. When a page is needed, the operating system checks to see if it is already in memory. If it is not, a page fault occurs and the operating system must bring the page into memory.
4. The operating system may need to evict a page from memory to make room for the new page. This is done using a page replacement algorithm.
5. Demand paging can improve the performance of a system by reducing the amount of memory required and by reducing the amount of time it takes to start a program.
6. However, if the system does not have enough memory, or if the page replacement algorithm is not effective, demand paging can cause thrashing, where the system spends most of its time swapping pages in and out of memory.
