# Concept Implementation for the Notes of the Unit 4 - Memory in the Subject of Computer Organization and Architecture

- Memory is an essential component of a computer system that stores and retrieves data and instructions.
- Memory can be classified into two types: primary memory and secondary memory.
- Primary memory is the main memory of the computer that is directly accessible by the CPU. It is also known as RAM (Random Access Memory).
- Secondary memory is the auxiliary memory of the computer that is not directly accessible by the CPU. It is also known as ROM (Read Only Memory), cache memory, magnetic disk, magnetic tape, optical disk, etc.
- Memory organization refers to the way how the memory cells are arranged and accessed by the CPU.
- Memory organization can be divided into three levels: instruction set architecture, memory hierarchy, and virtual memory.

## Instruction Set Architecture

- Instruction set architecture (ISA) is the interface between the hardware and the software of a computer system. It defines the format, encoding, and semantics of the instructions that the CPU can execute.
- ISA also specifies the registers, addressing modes, data types, and interrupt mechanisms of the CPU.
- ISA can be classified into two types: RISC (Reduced Instruction Set Computer) and CISC (Complex Instruction Set Computer).
- RISC is a type of ISA that uses simple and uniform instructions that can be executed in one clock cycle. RISC has fewer and smaller registers, fewer addressing modes, and simpler instruction formats than CISC.
- CISC is a type of ISA that uses complex and variable-length instructions that can perform multiple operations in one instruction. CISC has more and larger registers, more addressing modes, and more instruction formats than RISC.
- RISC and CISC have different advantages and disadvantages in terms of performance, power consumption, code size, and compatibility.

## Memory Hierarchy

- Memory hierarchy is the arrangement of different types of memory in a computer system according to their speed, size, and cost.
- Memory hierarchy consists of several levels of memory, such as registers, cache, main memory, and secondary memory.
- The higher levels of memory are faster, smaller, and more expensive than the lower levels of memory.
- The lower levels of memory are slower, larger, and cheaper than the higher levels of memory.
- The CPU accesses the memory from the highest level to the lowest level, depending on the availability and locality of the data and instructions.
- Memory hierarchy aims to optimize the performance and cost of the computer system by using the principle of locality and the technique of caching.

## Virtual Memory

- Virtual memory is a technique that allows the computer system to use more memory than the physical memory available.
- Virtual memory creates an illusion of a large and contiguous memory space for the programs and the CPU by using the secondary memory as an extension of the main memory.
- Virtual memory divides the logical address space of a program into fixed-size units called pages, and the physical address space of the main memory into fixed-size units called frames.
- Virtual memory maps the pages to the frames using a data structure called page table, which is stored in the main memory or a special cache called translation lookaside buffer (TLB).
- Virtual memory uses two techniques to manage the pages and frames: page replacement and page allocation.
- Page replacement is the technique of selecting a victim page from the main memory to be replaced by a new page from the secondary memory when the main memory is full.
- Page allocation is the technique of assigning a free frame to a new page when the page is brought from the secondary memory to the main memory.
- Virtual memory improves the utilization and protection of the main memory, and allows the execution of large and multiple programs simultaneously.