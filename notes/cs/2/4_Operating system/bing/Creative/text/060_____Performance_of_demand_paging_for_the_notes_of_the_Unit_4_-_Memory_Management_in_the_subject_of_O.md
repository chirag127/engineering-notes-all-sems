### Performance of demand paging

- Demand paging is a memory management technique that allows a process to access its virtual memory pages only when they are needed, rather than loading them all into physical memory at once  .
- The performance of demand paging is often measured in terms of the effective access time  , which is the average or expected time it takes to access memory, if the cost of page faults are amortized over all memory accesses.
- A page fault occurs when a process tries to access a page that is not present in physical memory, and the operating system has to bring it from the disk or swap space   .
- The effective access time can be calculated as  :

  - `effective access time = (1 - p) x ma + p x page fault time`
  - where `p` is the probability of a page fault (0 ≤ p ≤ 1), and `ma` is the memory access time (usually 10 to 200 nanoseconds).
  - The page fault time consists of the following components  :
    - Service the page fault interrupt
    - Read in the page from the disk or swap space
    - Update the page table and other data structures
    - Restart the instruction that caused the page fault
- The performance of demand paging depends on various factors, such as :
  - The page size: The larger the page size, the less the number of page tables required, which can result in faster memory access times. However, larger page sizes also increase the internal fragmentation and the disk transfer time.
  - The page replacement algorithm: The page replacement algorithm decides which page to evict from physical memory when a page fault occurs. The algorithm should minimize the number of page faults and the disk I/O operations.
  - The degree of multiprogramming: The degree of multiprogramming is the number of processes that are in memory at the same time. The higher the degree of multiprogramming, the more physical memory is utilized, but also the more page faults and disk contention may occur.
  - The locality of reference: The locality of reference is the tendency of a process to access the same or nearby pages repeatedly. The higher the locality of reference, the lower the probability of a page fault, and the better the performance of demand paging.
- The advantages of demand paging are:
  - Memory can be used more efficiently, as only the pages that are needed are loaded into physical memory.
  - A large virtual memory can be supported, as the size of the virtual memory is not limited by the size of the physical memory.
  - Programs that are larger than physical memory can be run, as the pages can be swapped in and out as needed.