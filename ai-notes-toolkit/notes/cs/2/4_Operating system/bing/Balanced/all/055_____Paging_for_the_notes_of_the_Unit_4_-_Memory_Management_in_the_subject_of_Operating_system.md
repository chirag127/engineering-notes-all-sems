# Paging

Paging is a memory management scheme that allows the operating system to store and retrieve data from secondary storage for use in main memory. In this scheme, the operating system retrieves data from secondary storage in same-size blocks called pages .

## Advantages of Paging

- Paging eliminates the need for contiguous allocation of physical memory, which reduces external fragmentation and simplifies memory allocation .
- Paging allows the physical address space of a process to be non-contiguous, which makes it possible to swap a process in and out of memory in a faster and more flexible way.
- Paging enables the use of virtual memory, which allows the execution of processes that are not completely in memory and increases the degree of multiprogramming .

## Example of Paging

Suppose the physical memory is divided into fixed-size frames of 4 KB each, and the logical memory is divided into pages of the same size. A process of size 10 KB will need three pages to store its code and data. The operating system will allocate three frames for this process and maintain a page table that maps the logical addresses to the physical addresses. The page table for this process may look like this:

| Page Number | Frame Number |
| ----------- | ------------ |
| 0           | 5            |
| 1           | 9            |
| 2           | 2            |

The page table is stored in a register or in a special memory area. When the process executes, the CPU generates logical addresses that consist of a page number and an offset within the page. The page number is used to index the page table and find the corresponding frame number. The frame number and the offset are combined to form the physical address that is sent to the memory unit. For example, if the CPU generates the logical address 0x0006, which means page 0 and offset 6, the page table will map it to the physical address 0x1406, which means frame 5 and offset 6.