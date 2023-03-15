### Demand Paging

Demand paging is a memory management technique used in operating systems where pages are loaded into memory only when they are needed. This is in contrast to pre-paging, where pages are loaded into memory before they are needed.

Some key points to remember about demand paging are:

1. Demand paging is used to reduce the amount of physical memory required by a program.
2. Pages are loaded into memory only when they are needed, which can reduce the time it takes to start a program.
3. When a page is needed but not present in memory, a page fault occurs, and the operating system must bring the page into memory from secondary storage.
4. The operating system uses a page replacement algorithm to decide which page to remove from memory when a new page needs to be loaded.
5. Demand paging can increase the amount of disk I/O required, as pages must be read from secondary storage when they are needed.
6. The effectiveness of demand paging depends on the locality of reference of the program, which is the tendency of the program to access the same pages repeatedly.