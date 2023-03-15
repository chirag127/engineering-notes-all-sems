### Performance of demand paging

- Demand paging is a memory management technique used in operating systems to divide a process’s virtual memory into fixed-sized pages and load them into the main memory only when they are needed or demanded by the CPU.
- Demand paging can significantly affect the performance of a computer system. To measure the performance of demand paging, we need to compute the effective access time for a demand-paged memory  .
- The effective access time is the average time required to access a page in memory, taking into account the possibility of a page fault.
- Let ma be the memory-access time, which ranges from 10 to 200 nanoseconds .
- Let p be the probability of a page fault, which is a fraction between 0 and 1. We would expect p to be close to zero, that is, we would expect to have only a few page faults.
- Let pf be the page fault service time, which is the time required to handle a page fault. This time includes the time to swap out a page (if needed), swap in the required page, update the page table, and restart the process.
- The effective access time can be calculated as follows:

```
effective access time = (1 - p) x ma + p x pf
```

- The effective access time depends on various factors, such as the page size, the page replacement algorithm, the degree of multiprogramming, the locality of reference, and the disk access time.
- The performance of demand paging can be improved by using various techniques, such as:

  - Increasing the page size to reduce the number of page tables and page faults, but not too large to cause internal fragmentation and waste of memory.
  - Choosing a suitable page replacement algorithm that minimizes the number of page faults and maximizes the hit ratio.
  - Implementing a prepaging strategy that brings in more than one page at a time to reduce the number of page faults.
  - Using a working set model to keep track of the pages that are currently in use by a process and allocate memory accordingly.
  - Implementing a local or global page replacement policy that balances the memory allocation among the processes.
  - Using a disk scheduling algorithm that optimizes the disk access time and reduces the page fault service time.