Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of process address space for the notes of the unit 3 - CPU scheduling in the subject of operating system.

### Process address space

- A process address space is the set of logical addresses that a process can access in its execution.
- A process address space consists of the following segments:
  - Text segment: This segment contains the executable code of the process. It is usually read-only and shared among all instances of the same program.
  - Data segment: This segment contains the global and static variables of the process. It is initialized by the program and can be read and written by the process.
  - Heap segment: This segment contains the dynamically allocated memory of the process. It grows and shrinks as the process requests and releases memory at run time.
  - Stack segment: This segment contains the local variables and function call information of the process. It grows and shrinks as the process enters and exits functions.
- A process address space is mapped to the physical memory by the operating system using a technique called virtual memory. Virtual memory allows the process to access more memory than the available physical memory by swapping some pages of the process to the disk when they are not needed.
- A process address space is divided into fixed-size units called pages. The physical memory is divided into fixed-size units called frames. The operating system maintains a data structure called a page table that records the mapping between the pages and the frames. The page table is stored in the memory and accessed by the hardware when the process performs a memory access.
- A process address space can be shared by multiple processes using a technique called memory mapping. Memory mapping allows a process to map a file or a portion of another process's address space into its own address space. This enables the process to access the file or the shared memory as if it were part of its own memory. Memory mapping can improve the performance and the efficiency of the system by reducing the disk I/O and the memory duplication.