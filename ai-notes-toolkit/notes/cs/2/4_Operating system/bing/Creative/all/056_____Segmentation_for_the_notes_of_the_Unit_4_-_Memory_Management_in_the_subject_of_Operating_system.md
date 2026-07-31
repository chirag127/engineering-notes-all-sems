# Segmentation in Operating System

- Segmentation is an operating system memory management technique that divides the user program and the secondary memory into uneven-sized blocks known as segments or sections .
- Segmentation is similar to paging, which divides the memory into fixed-sized blocks, but segments can have variable sizes and can be stored in non-contiguous memory locations .
- Segmentation allows the user to view the memory as a collection of independent modules or segments, each containing a piece of code, data, or stack .
- Segmentation has the following advantages :
  - It is closer to the programmer's view of the program structure and logical memory.
  - It avoids internal fragmentation, which occurs when a fixed-sized block is allocated to a process that requires less memory than the block size.
  - It reduces the CPU overhead, as it loads an entire module at once and does not need to perform address translation for each page.
  - It allows dynamic memory allocation, as segments can grow or shrink during execution and can be swapped in and out of memory as needed.
  - It provides protection and sharing, as each segment has its own access rights and can be shared among different processes.
- Segmentation has the following disadvantages:
  - It suffers from external fragmentation, which occurs when the memory space is not fully utilized due to the gaps between segments.
  - It requires more memory management, as the operating system has to maintain a segment table for each process and a free space list for the available memory.
  - It increases the address size, as each logical address consists of a segment number and an offset within the segment.
- Segmentation can be implemented in two ways:
  - Simple segmentation, where each process is divided into a number of segments, all of which are loaded into memory at run time and remain there until the process terminates.
  - Virtual memory segmentation, where each process is divided into a number of segments, not all of which are resident in memory at any time, and the operating system performs the necessary swapping and loading of segments on demand.