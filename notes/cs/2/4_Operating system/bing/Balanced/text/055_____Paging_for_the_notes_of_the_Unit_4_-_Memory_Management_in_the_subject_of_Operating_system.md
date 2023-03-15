### Paging

Paging is a memory management scheme that allows the operating system to store and retrieve data from secondary storage for use in main memory. In this scheme, the operating system retrieves data from secondary storage in same-size blocks called pages .

Some of the main points about paging are:

- Paging eliminates the need for contiguous allocation of physical memory, which reduces external fragmentation and simplifies memory allocation.
- Paging allows the physical address space of a process to be non-contiguous, which enables faster and more efficient swapping of processes.
- Paging also allows the logical address space of a process to be larger than the physical address space, which enables virtual memory and memory protection.
- Paging requires a data structure called a page table to map the logical addresses to the physical addresses. The page table is stored in main memory and accessed by the CPU during address translation .
- Paging involves an additional bit called the valid/invalid bit, which indicates whether a page is present in main memory or not. If a page is not present, a page fault occurs and the operating system has to bring the page from secondary storage .
- Paging may introduce internal fragmentation, as the last page of a process may not be completely filled. The size of a page is usually a power of two, ranging from 512 bytes to 16 megabytes .
- Paging may also increase the overhead of address translation, as the CPU has to access the page table for every memory reference. This can be reduced by using a cache called a translation look-aside buffer (TLB) that stores the most frequently used page table entries .
- Paging can be combined with other memory management schemes, such as segmentation, to provide more flexibility and functionality .