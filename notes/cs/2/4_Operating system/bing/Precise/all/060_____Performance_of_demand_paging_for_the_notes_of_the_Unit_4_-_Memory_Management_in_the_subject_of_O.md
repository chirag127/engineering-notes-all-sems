# Performance of Demand Paging

Demand paging is a technique used in operating systems to bring a page into the main memory only when it is needed or demanded by the CPU. This technique can significantly affect the performance of a computer system.

- The effective access time for a demand-paged memory can be computed by considering the memory-access time, denoted as `ma`, which ranges from 10 to 200 nanoseconds .
- The performance of demand paging depends on various factors, such as the page size. The larger the page size, the less the number of page tables required, which can result in faster memory access times.
- Let `p` be the probability of a page fault (0 ⩽ p ⩽ 1). We would expect `p` to be close to zero—that is, we would expect to have only a few page faults. The effective access time is then calculated as: `effective access time = (1 - p) x ma + p x page fault time`.

Demand paging has several advantages, including more efficient use of memory and the ability to run programs that are larger than physical memory. However, the performance of demand paging can be affected by various factors and must be carefully considered when implementing this technique in an operating system.