### Performance of demand paging

- Demand paging is a memory management technique that allows the operating system to load pages of a process into the main memory only when they are needed, rather than loading the entire process at once  .
- Demand paging can improve the performance of the system by reducing the number of page faults, which are the situations when a requested page is not found in the main memory and has to be brought from the secondary storage  .
- The performance of demand paging can be measured by the effective access time (EAT), which is the average time required to access a page in the main memory  .
- The EAT can be calculated as follows :

  - Let *p* be the probability of a page fault (0 ≤ *p* ≤ 1). We would expect *p* to be close to zero, meaning that most of the page requests can be satisfied by the main memory.
  - Let *ma* be the memory access time, which is the time required to access a page in the main memory. This is usually in the range of 10 to 200 nanoseconds.
  - Let *pf* be the page fault service time, which is the time required to handle a page fault. This includes the time to find the page in the secondary storage, transfer it to the main memory, update the page table, and restart the process. This is usually much larger than *ma*, in the range of milliseconds to seconds.
  - Then, the EAT can be expressed as:

    EAT = (1 - *p*) x *ma* + *p* x *pf*

- The performance of demand paging can be improved by using various techniques, such as:

  - Choosing an appropriate page size, which can balance the trade-off between the number of page tables, the internal fragmentation, and the transfer time.
  - Implementing a suitable page replacement algorithm, which can minimize the number of page faults by selecting the best page to evict from the main memory when it is full .
  - Using a prefetching strategy, which can anticipate the future page requests and load them into the main memory in advance .
  - Applying a locality principle, which can exploit the tendency of a process to access pages that are close to each other in space or time .