### Basic concept and hierarchy for the notes of the Unit 4 - Memory in the subject of Computer Organization and Architecture

- Memory is the component of a computer system that stores data and instructions for processing.
- Memory hierarchy is the arrangement of memory and storage devices in a computer system according to their speed, capacity, and cost.
- The purpose of memory hierarchy is to minimize the average access time of the entire memory system by exploiting the principle of locality of reference, which states that a program tends to access a small subset of its address space frequently.
- The memory hierarchy consists of several levels of memory, each with different characteristics and functions. The levels are:

  - **Register**: The fastest and smallest level of memory, located inside the CPU. It holds the data and instructions that are currently being executed by the CPU.
  - **Cache memory**: A small and fast level of memory, located close to the CPU. It acts as a buffer between the CPU and the main memory, and stores frequently accessed data and instructions.
  - **Main memory**: The largest and slowest level of memory, located outside the CPU. It holds the data and instructions that are currently needed by the CPU, and can be accessed directly by the CPU.
  - **Secondary memory**: The lowest and cheapest level of memory, located outside the computer system. It holds the data and instructions that are not currently needed by the CPU, and can be accessed indirectly by the CPU through the main memory. Examples of secondary memory are hard disk, optical disk, flash drive, etc.

- The memory hierarchy can be represented by the following diagram:

```
+----------+     +----------+
| Register | <-- | Cache    |
+----------+     +----------+
                  | Main     |
                  +----------+
                  | Secondary|
                  +----------+
```

- The memory hierarchy follows the following properties:

  - The higher the level, the faster, smaller, and more expensive the memory.
  - The lower the level, the slower, larger, and cheaper the memory.
  - The higher the level, the more frequently accessed the data and instructions.
  - The lower the level, the less frequently accessed the data and instructions.
  - The higher the level, the closer to the CPU the memory.
  - The lower the level, the farther from the CPU the memory.