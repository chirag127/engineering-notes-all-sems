### Segmentation in Operating System

- Segmentation is an operating system memory management technique that divides the user program and the secondary memory into uneven-sized blocks known as segments or sections .
- Segmentation is similar to paging, which is another memory management technique that divides the memory into fixed-sized blocks. However, segmentation is more flexible and closer to the programmer's view of physical memory.
- Segmentation has many advantages, such as:
  - It prevents internal fragmentation, which is the wasted space within a memory block that is not used by the process.
  - It reduces CPU overhead, because it contains an entire module at once, and does not require page table lookups.
  - It allows for dynamic memory allocation, which means that segments can grow or shrink as needed.
  - It supports protection and sharing, because each segment has its own access rights and can be shared among processes.
- Segmentation has some disadvantages, such as:
  - It causes external fragmentation, which is the wasted space between memory blocks that is not used by any process.
  - It requires more memory for storing segment tables, which map the logical addresses to physical addresses of segments.
  - It increases the complexity of memory management, because segments can vary in size and location.
- There are two types of segmentation in operating system:
  - Virtual memory segmentation, which is used to support large programs that do not fit entirely in the main memory. In this type, each process is divided into a number of segments, not all of which are resident at any time. The segments are swapped in and out of the memory as needed.
  - Simple segmentation, which is used to support modular programming and dynamic memory allocation. In this type, each process is divided into a number of segments, all of which are loaded into the memory at run time. The segments can be relocated and resized during execution.