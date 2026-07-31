### Performance of demand paging

- Demand paging is a memory management technique that allows the operating system to load pages of a process into the main memory only when they are needed, rather than loading the entire process at once  .
- Demand paging can improve the performance of the system by reducing the number of disk I/O operations, increasing the degree of multiprogramming, and allowing the use of virtual memory .
- However, demand paging also introduces the possibility of page faults, which occur when a requested page is not present in the main memory and has to be brought from the disk .
- Page faults can significantly increase the effective access time of memory, which is the average time required to access a word in memory .
- The effective access time can be calculated as follows :

  - Let *p* be the probability of a page fault (0 ≤ *p* ≤ 1).
  - Let *ma* be the memory access time, which is the time to access a word in memory without any page fault.
  - Let *pf* be the page fault service time, which is the time to handle a page fault and bring the page from the disk to the memory.
  - Then, the effective access time is:

    - effective access time = (1 - *p*) x *ma* + *p* x *pf*

- The performance of demand paging depends on various factors, such as :

  - The page size: The larger the page size, the less the number of page tables required, which can result in faster memory access times. However, larger page sizes also increase the internal fragmentation and the disk transfer time.
  - The page replacement algorithm: The page replacement algorithm determines which page to evict from the memory when a page fault occurs. The algorithm should minimize the number of page faults and the overhead of maintaining the page tables.
  - The degree of locality: The degree of locality refers to how frequently a process accesses the same set of pages. The higher the degree of locality, the lower the probability of page faults.