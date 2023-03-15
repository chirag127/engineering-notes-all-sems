### Virtual memory concepts

- Virtual memory is a method that computers use to manage storage space to keep systems running quickly and efficiently.
- Virtual memory uses both hardware and software to enable a computer to compensate for physical memory shortages, temporarily transferring data from random access memory (RAM) to disk storage.
- Virtual memory makes application programming easier by hiding fragmentation of physical memory; by delegating to the kernel the burden of managing the memory hierarchy; and, when each process is run in its own dedicated address space, by obviating the need to relocate program code or data.
- Virtual memory is implemented using a technique called paging, which divides the logical address space of a process into fixed-size units called pages, and the physical memory into units called frames.
- The operating system maintains a data structure called a page table for each process, which maps the logical addresses of the pages to the physical addresses of the frames where they are stored.
- When a process accesses a page that is not in the physical memory, a page fault occurs, and the operating system has to bring the page from the disk to the memory, and update the page table accordingly.
- The operating system may use a replacement algorithm to decide which page to evict from the memory when there is no free frame available.
- The operating system may also use a fetch policy to determine when to load a page into the memory, either on demand (when it is accessed) or in advance (when it is anticipated to be accessed).
- The operating system may also use a placement policy to decide where to place a page in the physical memory, either in a fixed or a variable location.
- The operating system may also use a cleaning policy to determine when to write a modified page back to the disk, either immediately (write-through) or later (write-back).
- The performance of virtual memory depends on several factors, such as the size of the pages and frames, the number of page faults, the disk access time, and the replacement algorithm.
- Virtual memory has several advantages, such as allowing more processes to run concurrently, enabling dynamic linking and loading of libraries, supporting memory protection and security, and facilitating memory sharing and mapping .
- Virtual memory also has some disadvantages, such as increasing the complexity and overhead of the operating system, causing external fragmentation of the disk space, and introducing the possibility of thrashing, which occurs when the system spends more time swapping pages than executing processes .