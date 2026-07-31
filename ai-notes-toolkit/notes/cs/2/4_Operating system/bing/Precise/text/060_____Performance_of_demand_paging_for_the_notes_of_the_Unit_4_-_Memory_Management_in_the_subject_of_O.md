### Performance of Demand Paging

Demand paging is a technique in which a page is usually brought into the main memory only when it is needed or demanded by the CPU. Initially, only those pages are loaded that are required by the process immediately. Those pages that are never accessed are thus never loaded into the physical memory.

Demand paging can significantly affect the performance of a computer system. To see why, let’s compute the effective access time for a demand-paged memory. The memory-access time, denoted ma, ranges from 10 to 200 nanoseconds .

Let p be the probability of a page fault (0 ⩽ p ⩽ 1). We would expect p to be close to zero—that is, we would expect to have only a few page faults. The effective access time is then effective access time = (1 - p) x ma + p x page fault time.

The advantages of demand paging are: Memory can be used more efficiently. If we use demand paging, then we can have a large virtual memory. By using demand paging, we can run programs that are larger than physical memory.

The performance of paging depends on various factors, such as: Page size: The larger the page size, the less the number of page tables required, which can result in faster memory access times.