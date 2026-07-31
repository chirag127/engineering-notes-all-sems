 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Basic bare machine for the notes of the Unit 4 - Memory Management in the subject of Operating system

1. Memory: Memory refers to the volatile storage space in the computer. It is primarily used to store the program instructions and data. The memory is classified into primary and secondary memory.
- Primary memory: It refers to the main memory of the computer which is directly accessed by the CPU. It is volatile in nature. Examples are RAM and ROM.
- Secondary memory: It refers to the additional storage provided to store data and programs. It is non-volatile in nature. Examples are hard drives, CDs, etc.
2. Memory hierarchy: The memory is organized into a hierarchy based on the characteristics like speed, cost per bit, capacity, etc. The levels of memory hierarchy from fastest to slowest access time are:
- Processor registers
- Cache memory
- Main memory (RAM)
- Secondary storage (Hard drives)
3. Memory management: It refers to the process of controlling and coordinating the computer memory. The key tasks involved are:
- Keeping track of which parts of memory are currently being used and by whom.
- Deciding which processes should be loaded into memory when memory space becomes available.
- Allocating and de-allocating memory space as needed.
- Shuffling programs and data in and out of memory to make more efficient use of memory.
4. Memory allocation: It refers to the process of assigning memory space to programs when they request and release the memory space when it is no longer required. The key memory allocation techniques are:
- Contiguous allocation: The entire block of memory is allocated to the process.
- Fragmentation: The memory gets fragmented into small chunks and hence results in inefficient usage of memory.
- Paging: The memory is divided into fixed sized blocks called pages. The pages required by the process are allocated and the unused ones are de-allocated. This technique avoids external fragmentation.
- Segmentation: The memory is divided into variable sized segments. Each process is allocated the segments it needs. This technique avoids internal fragmentation.