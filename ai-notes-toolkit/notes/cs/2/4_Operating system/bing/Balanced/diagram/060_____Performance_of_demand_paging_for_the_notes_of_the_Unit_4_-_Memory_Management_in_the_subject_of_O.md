### Performance of demand paging

Demand paging is a memory management technique that allows the operating system to load pages of a process from the secondary storage into the main memory only when they are needed. This reduces the amount of physical memory required and allows the execution of programs that are larger than the available memory.

The performance of demand paging depends on several factors, such as:

- The probability of a page fault, denoted by p, which is the fraction of memory accesses that cause a page fault. A page fault occurs when the requested page is not present in the main memory and needs to be fetched from the disk. The value of p is usually close to zero, meaning that most of the memory accesses are to pages that are already in memory.
- The memory access time, denoted by ma, which is the time required to access a word from the main memory. The value of ma is typically in the range of 10 to 200 nanoseconds.
- The page fault service time, denoted by pf, which is the time required to handle a page fault. This includes the time to find a free frame in the main memory, to read the page from the disk, to update the page table, and to restart the instruction that caused the page fault. The value of pf is typically in the range of 1 to 100 milliseconds.

The effective access time, denoted by ea, is the average time required to access a word from the memory, taking into account the possibility of page faults. The effective access time can be calculated as follows:

ea = (1 - p) x ma + p x pf

The effective access time is a weighted average of the memory access time and the page fault service time, where the weights are the probabilities of having a page hit or a page fault. The effective access time is directly proportional to the probability of a page fault and the page fault service time, and inversely proportional to the memory access time.

The performance of demand paging can be improved by reducing the probability of a page fault or the page fault service time. Some of the techniques that can be used to achieve this are:

- Choosing an appropriate page size. The page size affects the number of page table entries, the internal fragmentation, the disk transfer time, and the degree of locality. A larger page size reduces the number of page table entries and the disk transfer time, but increases the internal fragmentation and the probability of a page fault. A smaller page size reduces the internal fragmentation and the probability of a page fault, but increases the number of page table entries and the disk transfer time. Therefore, there is a trade-off between the page size and the performance of demand paging.
- Using a suitable page replacement algorithm. The page replacement algorithm determines which page to evict from the main memory when a page fault occurs and a free frame is not available. The goal of the page replacement algorithm is to minimize the number of page faults by choosing the page that is least likely to be referenced in the near future. Some of the common page replacement algorithms are FIFO, LRU, OPT, and CLOCK.
- Implementing a prefetching policy. The prefetching policy decides when and how many pages to load into the main memory in advance, before they are actually requested by the process. The goal of the prefetching policy is to reduce the page fault service time by overlapping the disk I/O with the CPU execution. Some of the factors that affect the prefetching policy are the available memory space, the disk bandwidth, the locality of reference, and the predictability of the page references.