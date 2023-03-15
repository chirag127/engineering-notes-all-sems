### Performance of demand paging

Demand paging is a memory management technique that allows the operating system to load pages of a process from the secondary storage into the main memory only when they are needed. This reduces the amount of physical memory required and allows the execution of programs that are larger than the available memory.

The performance of demand paging depends on several factors, such as:

- The probability of a page fault, denoted by p, which is the fraction of memory accesses that cause a page fault. A page fault occurs when the requested page is not present in the main memory and needs to be fetched from the disk. The value of p is expected to be close to zero, as most memory accesses are likely to hit the pages that are already in memory.
- The memory access time, denoted by ma, which is the time required to access a word from the main memory. The value of ma is typically in the range of 10 to 200 nanoseconds.
- The page fault service time, denoted by pf, which is the time required to handle a page fault. This includes the time to find a free frame in the main memory, to read the page from the disk, to update the page table, and to restart the instruction that caused the page fault. The value of pf is typically in the range of milliseconds, which is much larger than ma.

The effective access time, denoted by ea, is the average time required to access a word from the memory, taking into account the possibility of page faults. The effective access time can be calculated as follows:

ea = (1 - p) x ma + p x pf

The effective access time is a measure of the performance of demand paging. The lower the effective access time, the better the performance. The performance of demand paging can be improved by using various techniques, such as:

- Choosing an appropriate page size, which is the size of each page in bytes. The page size affects the number of page tables required, the internal fragmentation, the disk transfer time, and the page fault rate. There is no optimal page size that works for all situations, as different page sizes have different trade-offs.
- Using a suitable page replacement algorithm, which is the algorithm that decides which page to evict from the main memory when a page fault occurs and there is no free frame available. The page replacement algorithm affects the page fault rate, as some algorithms can reduce the number of page faults by choosing the pages that are least likely to be used in the near future. Some common page replacement algorithms are FIFO, LRU, OPT, and CLOCK.
- Implementing a prefetching mechanism, which is the technique of loading pages into the main memory before they are actually needed. This can reduce the page fault rate by anticipating the future memory accesses and avoiding unnecessary page faults. However, prefetching also has some drawbacks, such as wasting memory space, increasing disk traffic, and causing thrashing.
- Applying a locality principle, which is the observation that programs tend to access a relatively small subset of pages at a given time. This implies that the pages that are recently accessed are likely to be accessed again in the near future, and the pages that are not accessed for a long time are unlikely to be accessed soon. The locality principle can be exploited by using a working set model, which is the technique of keeping only the pages that belong to the current working set of a process in the main memory. The working set model can improve the performance of demand paging by reducing the page fault rate and the memory utilization.