# Basic concept and hierarchy for the notes of the Unit 4 - Memory in the subject of Computer Organization and Architecture

- Memory is the component of a computer system that stores data and instructions for processing.
- Memory hierarchy is the arrangement of memory and storage devices in a computer system according to their speed, capacity, and cost.
- The purpose of memory hierarchy is to minimize the average access time of the entire memory system by exploiting the principle of locality of reference, which states that a program tends to access a small subset of its address space frequently and repeatedly.
- The memory hierarchy consists of several levels of memory, each with different characteristics and functions. The levels are:

  - **Register**: The fastest and smallest level of memory, located inside the CPU. It holds the data and instructions that are currently being executed by the CPU.
  - **Cache memory**: A small and fast level of memory, located close to the CPU. It acts as a buffer between the CPU and the main memory, and stores frequently accessed data and instructions.
  - **Main memory**: Also known as primary memory or random access memory (RAM), it is the largest and most commonly used level of memory. It holds the data and instructions that are currently needed by the CPU and the programs running on the computer.
  - **Secondary memory**: Also known as auxiliary memory or external memory, it is the slowest and cheapest level of memory. It provides permanent and large storage for data and instructions that are not currently needed by the CPU or the programs. Examples of secondary memory are hard disk, optical disk, flash memory, etc.

- The figure below shows a diagram of the memory hierarchy:

![Memory hierarchy diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/ComputerMemoryHierarchy.svg/1200px-ComputerMemoryHierarchy.svg.png)

- The memory hierarchy design is based on the following trade-offs:

  - **Speed**: The higher the level of memory, the faster it is, but also the smaller and more expensive it is.
  - **Capacity**: The lower the level of memory, the larger and cheaper it is, but also the slower it is.
  - **Locality**: The higher the level of memory, the more likely it is to contain the data and instructions that are needed by the CPU, but also the more complex and costly it is to manage.

- The memory hierarchy works by using the following techniques:

  - **Temporal locality**: If a data or instruction is accessed once, it is likely to be accessed again soon. Therefore, it is copied from a lower level of memory to a higher level of memory, where it can be accessed faster.
  - **Spatial locality**: If a data or instruction is accessed once, it is likely that the nearby data or instructions will be accessed soon. Therefore, a block or a group of data or instructions is copied from a lower level of memory to a higher level of memory, where it can be accessed faster.
  - **Mapping**: A mechanism that determines how a data or instruction is located and transferred between different levels of memory. There are different types of mapping, such as direct, associative, or set-associative.
  - **Replacement**: A policy that decides which data or instruction to remove from a higher level of memory when it is full and a new data or instruction needs to be copied from a lower level of memory. There are different types of replacement, such as least recently used (LRU), first in first out (FIFO), or random.
  - **Write**: A strategy that determines how a data or instruction is updated in different levels of memory when it is modified by the CPU. There are different types of write, such as write-through, write-back, or write-allocate.