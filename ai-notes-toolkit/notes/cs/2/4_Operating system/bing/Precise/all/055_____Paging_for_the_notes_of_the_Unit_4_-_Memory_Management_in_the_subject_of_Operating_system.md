### Paging

Paging is a memory management technique used by operating systems to manage the allocation of physical memory to processes. It allows the physical memory to be divided into fixed-size blocks called frames, and the logical memory of a process to be divided into blocks of the same size called pages.

- When a process is executed, its pages are loaded into available memory frames.
- The operating system maintains a page table for each process, which keeps track of the mapping between the pages of the process and the frames in physical memory.
- When a process references a memory location, the operating system uses the page table to translate the logical address into a physical address.
- If the referenced page is not currently in memory, a page fault occurs and the operating system must bring the page into memory from secondary storage.
- Paging allows the operating system to use the physical memory more efficiently by allocating memory to processes on a page-by-page basis, rather than allocating a contiguous block of memory to each process.
- It also allows the operating system to implement virtual memory, where the logical memory of a process can be larger than the available physical memory.