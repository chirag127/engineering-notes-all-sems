### Protection schemes for the notes of the Unit 4 - Memory Management in the subject of Operating system

1. **Base and Limit Registers**: A base register holds the smallest legal physical memory address, while a limit register specifies the size of the range. The operating system must ensure that a program never attempts to access memory outside of its allocated range.

2. **Memory Partitioning**: Memory partitioning is the process of dividing the main memory into multiple logical sections, each of which can be allocated to a different process. This helps to prevent one process from accessing the memory space of another process.

3. **Paging**: Paging is a memory management technique that allows the physical address space of a process to be non-contiguous. The operating system maintains a page table for each process, which maps virtual addresses to physical addresses. This helps to prevent one process from accessing the memory space of another process.

4. **Segmentation**: Segmentation is a memory management technique that allows a program to be divided into multiple segments, each of which can be allocated to a different area of memory. The operating system maintains a segment table for each process, which maps segment numbers to physical addresses. This helps to prevent one process from accessing the memory space of another process.

5. **Access Control**: Access control is the process of determining what actions a user or process is allowed to perform on a system. This can include determining what memory locations a process is allowed to access. Access control can be implemented using techniques such as access control lists or role-based access control.

6. **Virtual Memory**: Virtual memory is a memory management technique that allows a process to use more memory than is physically available on the system. The operating system uses a combination of hardware and software to map virtual addresses to physical addresses, allowing the process to access memory that is not currently in physical memory. This helps to prevent one process from accessing the memory space of another process.