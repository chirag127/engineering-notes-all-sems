### Performance of Demand Paging

Demand paging is a memory management technique used in operating systems to divide a process’s virtual memory into fixed-sized pages. The performance of demand paging depends on various factors, such as:

- **Page size**: The larger the page size, the less the number of page tables required, which can result in faster memory access times.

- **Probability of a page fault**: Let p be the probability of a page fault (0 ⩽ p ⩽ 1). We would expect p to be close to zero—that is, we would expect to have only a few page faults. The effective access time is then effective access time = (1 - p) x ma + p x page fault time.

- **Advantages of demand paging**: It can improve performance by allowing the operating system to keep more programs and files in memory, thereby reducing the number of times that they need to be loaded from the disk. It can allow the operating system to use more memory than is physically installed by using virtual memory .

Demand paging can significantly affect the performance of a computer system. By using demand paging, we can run programs that are larger than physical memory.