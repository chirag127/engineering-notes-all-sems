# Paging

Paging is a memory management scheme that allows the operating system to store and retrieve data from secondary storage for use in main memory. In this scheme, the operating system retrieves data from secondary storage in same-size blocks called pages .

## Advantages of Paging

- Paging eliminates the need for contiguous allocation of physical memory, which reduces external fragmentation and compaction .
- Paging allows the physical address space of a process to be non-contiguous, which makes the process creation and swapping easier.
- Paging simplifies memory allocation, as any free page can be allocated to a process that needs more memory .
- Paging provides a mechanism for memory protection, as each page can have its own access permissions and valid/invalid bit .

## Disadvantages of Paging

- Paging introduces overhead in terms of time and space, as the operating system has to maintain a page table for each process and perform address translation for each memory access .
- Paging may cause internal fragmentation, as the last page of a process may not be completely filled .
- Paging may increase the number of disk I/O operations, as the operating system has to fetch pages from secondary storage when they are not present in main memory .
- Paging may degrade the performance of some applications that require sequential access to memory, as the pages may not be in the same order in main memory as in secondary storage .

## Example of Paging

Suppose the physical memory size is 64 KB and the page size is 4 KB. Then, the physical memory can be divided into 16 frames, each of size 4 KB. Suppose a process P has a logical address space of 20 KB, which can be divided into 5 pages, each of size 4 KB. Then, the operating system can allocate any 5 frames to the process P and store the mapping information in the page table of P. For example, the page table of P may look like this:

| Page Number | Frame Number | Valid/Invalid Bit |
| ----------- | ------------ | ----------------- |
| 0           | 5            | 1                 |
| 1           | 9            | 1                 |
| 2           | 2            | 1                 |
| 3           | 14           | 1                 |
| 4           | 11           | 1                 |

This means that the page 0 of P is stored in the frame 5, the page 1 of P is stored in the frame 9, and so on. The valid/invalid bit indicates whether the page is present in main memory or not. A value of 1 means that the page is valid and present in main memory, and a value of 0 means that the page is invalid and not present in main memory .

Now, suppose the process P wants to access the logical address 12,456. To do this, the operating system has to perform the following steps:

- Divide the logical address into a page number and an offset. In this case, the page number is 12,456 / 4,096 = 3 and the offset is 12,456 % 4,096 = 268.
- Check the valid/invalid bit of the page 3 in the page table of P. If it is 0, then the page is not present in main memory and a page fault occurs. The operating system has to fetch the page 3 from secondary storage and load it into a free frame in main memory, and update the page table of P accordingly.
- If the valid/invalid bit of the page 3 is 1, then the page is present in main memory and no page fault occurs. The operating system can find the frame number of the page 3 in the page table of P, which is 14 in this example.
- Calculate the physical address by multiplying the frame number by the page size and adding the offset. In this case, the physical address is 14 * 4,096 + 268 = 57,644.
- Access the data at the physical address 57,644 in main memory .