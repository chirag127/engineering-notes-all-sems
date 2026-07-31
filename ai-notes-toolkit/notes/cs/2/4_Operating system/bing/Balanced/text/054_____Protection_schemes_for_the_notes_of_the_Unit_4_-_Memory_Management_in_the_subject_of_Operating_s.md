### Protection schemes for the notes of the Unit 4 - Memory Management in the subject of Operating system

- Memory protection is an important concept in operating system that prevents a process from accessing unallocated memory or memory that belongs to another process or the kernel .
- Memory protection is required to protect the operating system from user processes and to ensure the correct functioning of the programs.
- Memory protection can be implemented by using hardware or software mechanisms, or a combination of both.
- Some of the common protection schemes are:

  - **Base and limit registers**: These are special registers that store the base address and the size of the memory allocated to a process. The CPU checks every memory reference against these registers and generates an exception if the reference is invalid .
  - **Paging**: This is a technique that divides the physical memory into fixed-size blocks called pages and the logical memory into blocks of the same size called page frames. A page table maps the page frames to the pages and stores the protection bits for each page. The CPU uses the page table to translate the logical address to the physical address and to check the protection bits.
  - **Segmentation**: This is a technique that divides the logical memory into variable-size blocks called segments. Each segment has a base address, a limit, and a set of protection bits. A segment table maps the segments to the physical memory and stores the segment information. The CPU uses the segment table to translate the logical address to the physical address and to check the protection bits.
  - **Virtual memory**: This is a technique that allows the execution of processes that are not completely in the physical memory. The operating system uses a combination of paging and segmentation to manage the virtual memory. The operating system also uses a page replacement algorithm to swap the pages between the physical memory and the secondary storage.

- Some operating systems that implement memory protection include: Unix-like systems, Plan9 and Inferno, OS/2, RISC OS, Microsoft Windows, etc.