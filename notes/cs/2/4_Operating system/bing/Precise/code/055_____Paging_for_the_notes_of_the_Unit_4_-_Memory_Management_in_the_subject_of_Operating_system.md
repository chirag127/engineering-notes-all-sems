### Paging

Paging is a memory management technique used by operating systems to manage the allocation of physical memory to processes. It allows the physical memory to be divided into fixed-size blocks called frames, and the logical memory of a process to be divided into blocks of the same size called pages.

Here are some key points to remember about paging:

1. Paging allows the physical memory to be used more efficiently by allocating only the required amount of memory to a process.
2. The operating system maintains a page table for each process, which maps the virtual addresses of the process to the physical addresses of the frames.
3. When a process references a virtual address, the operating system uses the page table to translate the virtual address into a physical address.
4. If the required page is not present in the physical memory, a page fault occurs, and the operating system must bring the required page into memory from the secondary storage.
5. Paging can lead to fragmentation of the physical memory, as the frames may not be contiguous.
6. The size of the pages and frames is determined by the hardware and is typically a power of 2, such as 4KB or 8KB.
