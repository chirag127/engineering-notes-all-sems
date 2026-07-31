### Basic concept and hierarchy for the notes of the Unit 4 - Memory in the subject of Computer Organization and Architecture

- Memory is the component of a computer system that stores data and instructions for processing. Memory is divided into several levels based on the speed, capacity, cost and technology of the storage devices.
- Memory hierarchy is the arrangement of memory levels in a computer system, such that the memory level with the fastest access time and the lowest capacity is at the top, and the memory level with the slowest access time and the highest capacity is at the bottom. The purpose of memory hierarchy is to minimize the average access time of the entire memory system by exploiting the principle of locality of reference .
- Memory hierarchy diagram is a graphical representation of the memory hierarchy in a computer system. It shows the relative sizes, speeds and costs of the memory levels. A typical memory hierarchy diagram is shown below :

![Memory hierarchy diagram](https://www.gatevidyalay.com/wp-content/uploads/2018/07/Memory-Hierarchy-Diagram.png)

- The memory levels in the memory hierarchy are:

  - **Register**: The fastest and the smallest memory level, located inside the CPU. It stores the data and instructions that are currently being executed by the CPU. It has the lowest access time and the highest cost per bit.
  - **Cache memory**: The second fastest and the second smallest memory level, located between the CPU and the main memory. It stores the copies of the data and instructions that are frequently accessed by the CPU from the main memory. It has a low access time and a high cost per bit. It uses the principle of spatial and temporal locality to improve the hit ratio .
  - **Main memory**: The third fastest and the third smallest memory level, located outside the CPU. It stores the data and instructions that are currently needed by the CPU and the cache memory. It has a moderate access time and a moderate cost per bit. It is also known as the primary memory or the random access memory (RAM).
  - **Secondary memory**: The slowest and the largest memory level, located outside the CPU and the main memory. It stores the data and instructions that are not currently needed by the CPU and the main memory, but can be transferred to them when required. It has a high access time and a low cost per bit. It is also known as the auxiliary memory or the mass storage. Examples of secondary memory are hard disk, optical disk, magnetic tape, etc.

- The characteristics of the memory hierarchy are:

  - **Inclusion**: The data and instructions stored in a lower level of memory are also stored in all the higher levels of memory. For example, the data and instructions stored in the main memory are also stored in the cache memory and the register.
  - **Block transfer**: The data and instructions are transferred between the memory levels in the form of blocks or pages, rather than individual words or bytes. For example, when the CPU accesses a word from the main memory, the entire block containing that word is transferred to the cache memory.
  - **Locality of reference**: The data and instructions that are accessed by the CPU tend to be clustered in a small region of memory, rather than being scattered randomly. There are two types of locality of reference: spatial locality and temporal locality. Spatial locality means that the data and instructions that are near to the ones that are currently accessed are likely to be accessed in the near future. Temporal locality means that the data and instructions that are recently accessed are likely to be accessed again in the near future .
  - **Hit ratio**: The ratio of the number of times the data and instructions are found in a memory level to the total number of accesses to that memory level. For example, if the CPU accesses the cache memory 100 times and finds the data and instructions in the cache memory 80 times, then the hit ratio of the cache memory is 80/100 = 0.8 or 80%. The hit ratio is a measure of the effectiveness of a memory level. A higher hit ratio means a lower average access time .

: Memory hierarchy - Wikipedia
: Memory Hierarchy | Memory Hierarchy Diagram | Gate Vidyalay
: Memory Hierarchy Design and its Characteristics - GeeksforGeeks