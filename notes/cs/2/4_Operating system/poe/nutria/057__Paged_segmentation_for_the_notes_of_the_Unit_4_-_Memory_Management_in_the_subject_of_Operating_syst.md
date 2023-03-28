
### Paged Segmentation for Unit 4 - Memory Management in Operating Systems

1. Memory management is the process of allocating and managing computer memory.
2. Paging is a memory management technique that divides memory into fixed-sized pages, which are then stored in the main memory.
3. Each page is assigned a unique page number and is stored in a page table.
4. When a process requests memory, the operating system searches the page table for the page number associated with the requested memory.
5. If the page is not found in the page table, the operating system must perform a page fault, which is a process of loading the page into main memory from a secondary storage device (e.g. hard disk).
6. Once the page is loaded into main memory, the page table is updated with the page number and the memory is allocated to the process.
7. Paging is beneficial because it allows for efficient use of memory, as it allows for multiple processes to share the same memory space.
8. Additionally, paging allows for the operating system to swap out inactive pages from main memory to a secondary storage device, thus freeing up memory space for other processes.