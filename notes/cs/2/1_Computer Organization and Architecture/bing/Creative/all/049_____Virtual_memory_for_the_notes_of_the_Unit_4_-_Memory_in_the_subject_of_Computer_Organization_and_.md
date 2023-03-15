# Virtual Memory

- Virtual memory is a **technique** that allows the execution of programs that are not completely in physical memory.
- Virtual memory creates an **illusion** of a large main memory for the programmer, when in reality the physical memory is limited.
- Virtual memory uses some of the space from **secondary storage** (such as hard disk) and maps it to the **address space** of the process.
- Virtual memory allows **multiple processes** to share the physical memory and run concurrently, without interfering with each other.
- Virtual memory also enables **memory protection**, **relocation**, and **swapping** of processes.

## Characteristics of Virtual Memory

- Virtual memory is **transparent** to the programmer, meaning that the programmer does not need to know how the virtual memory is implemented or managed by the operating system.
- Virtual memory is **dynamic**, meaning that the mapping between the virtual addresses and the physical addresses can change during the execution of a process.
- Virtual memory is **hierarchical**, meaning that the virtual address space is divided into **pages** and the physical memory is divided into **frames**. A page is a fixed-size block of contiguous virtual addresses, and a frame is a fixed-size block of contiguous physical addresses. A page can be mapped to any frame in the physical memory, or to a location in the secondary storage if the page is not currently in use.
- Virtual memory is **demand-paged**, meaning that a page is only brought into the physical memory when it is needed by the process. This reduces the amount of physical memory required and allows the execution of programs that are larger than the physical memory.
- Virtual memory is **paged-replacement**, meaning that when the physical memory is full and a new page needs to be brought in, an existing page has to be **evicted** from the physical memory and written back to the secondary storage. The operating system uses a **replacement policy** to decide which page to evict, such as **least recently used (LRU)**, **first in first out (FIFO)**, or **random**.
- Virtual memory is **managed** by the operating system, with the help of the **hardware**. The hardware provides a **memory management unit (MMU)**, which is responsible for translating the virtual addresses to the physical addresses and checking the validity and protection of the pages. The MMU uses a **page table**, which is a data structure that stores the mapping information for each page. The page table is maintained by the operating system and updated whenever a page is brought in or evicted from the physical memory.