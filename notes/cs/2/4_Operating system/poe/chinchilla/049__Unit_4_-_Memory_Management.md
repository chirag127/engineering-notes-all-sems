## Unit 4 - Memory Management

Memory management is the process of controlling and coordinating computer memory, assigning portions called blocks to various running programs to optimize the overall performance of the system. In this unit, we will learn about the various memory management techniques and concepts.

### Memory Hierarchy

Memory Hierarchy is a pyramid-like structure consisting of different levels of memory, each level having different characteristics in terms of speed, cost, and capacity. The levels of memory hierarchy are:

- Cache Memory: It is a small, fast memory that stores frequently used data for quick access. It is located between the CPU and the main memory.
- Primary Memory: It is the main memory of the computer that stores data and instructions that are currently in use by the CPU. It is also known as RAM (Random Access Memory).
- Secondary Memory: It is a non-volatile memory that stores data and instructions permanently. Examples include hard disks, solid-state drives, and optical disks.
- Tertiary Memory: It is a backup storage system used for archiving and backup purposes. Examples include magnetic tapes and off-site storage.

### Memory Allocation

Memory allocation is the process of assigning memory blocks to running programs. There are two types of memory allocation:

- Static Memory Allocation: Memory is allocated to a program during compile time. The size of the memory block is fixed and cannot be changed during runtime.
- Dynamic Memory Allocation: Memory is allocated to a program during runtime. The size of the memory block can be changed during runtime.

### Memory Management Techniques

There are various memory management techniques used by operating systems, including:

- Paging: It is a memory management technique that divides the memory into fixed-size blocks called pages. Each page is stored in a separate location in the physical memory. The operating system keeps track of the pages allocated to each program in a page table.
- Segmentation: It is a memory management technique that divides the memory into variable-sized blocks called segments. Each segment contains a logical unit of data or code. The operating system keeps track of the segments allocated to each program in a segment table.
- Virtual Memory: It is a memory management technique that allows a program to use more memory than is physically available in the system. The operating system creates a virtual address space for each program and maps it to the physical memory as needed.

### Memory Fragmentation

Memory fragmentation occurs when the free memory available for allocation is divided into small, non-contiguous blocks. This can lead to inefficient use of memory and reduced performance. There are two types of memory fragmentation:

- Internal Fragmentation: It occurs when a program is allocated more memory than it actually requires, resulting in wasted memory.
- External Fragmentation: It occurs when free memory is divided into small, non-contiguous blocks, making it difficult to allocate large memory blocks to programs.

### Conclusion

Memory management is an essential aspect of operating systems that ensures efficient use of memory resources and optimization of system performance. Understanding the various memory management techniques and concepts is crucial for computer science students and professionals alike.