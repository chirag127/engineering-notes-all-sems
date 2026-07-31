# Virtual Memory

- Virtual memory is a **technique** that allows the execution of programs that are not completely in physical memory.
- Virtual memory creates an **illusion** of a large main memory for the programmer, when in reality the physical memory is limited.
- Virtual memory uses some of the space from **secondary storage** (such as hard disk) and maps it to the **address space** of the process.
- Virtual memory allows **multiple processes** to share the physical memory and run concurrently, without interfering with each other.
- Virtual memory also enables **memory protection**, **relocation**, and **swapping** of processes.

## Characteristics of Virtual Memory

- Virtual memory is **transparent** to the programmer, meaning that the programmer does not need to know how the virtual memory is implemented or managed by the operating system.
- Virtual memory is **dynamic**, meaning that the mapping between the virtual and physical addresses can change during the execution of a process, depending on the availability of physical memory and the demand of the process.
- Virtual memory is **hierarchical**, meaning that the virtual address space is divided into **pages** of fixed size, and the physical memory is divided into **frames** of the same size. A page can be mapped to any frame in the physical memory, or to a location in the secondary storage if the page is not in the physical memory.
- Virtual memory is **associative**, meaning that the mapping between the pages and the frames is not fixed, but can be changed by the operating system using a **page table**. A page table is a data structure that stores the mapping information for each page of a process.
- Virtual memory is **demand-paged**, meaning that a page is only brought into the physical memory when it is needed by the process, not when the process is loaded. This reduces the amount of physical memory required and allows the execution of larger programs than the physical memory can accommodate.
- Virtual memory is **paged-replacement**, meaning that when the physical memory is full and a new page is needed, the operating system must choose a page to **replace** or **evict** from the physical memory and write it back to the secondary storage. The choice of the page to replace is based on a **replacement algorithm** that tries to minimize the number of **page faults**. A page fault occurs when a process tries to access a page that is not in the physical memory.