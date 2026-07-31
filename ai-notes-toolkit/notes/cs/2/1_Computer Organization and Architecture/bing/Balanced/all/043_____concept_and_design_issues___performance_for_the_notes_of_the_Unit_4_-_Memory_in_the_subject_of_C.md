# Concept and Design Issues & Performance for the Notes of the Unit 4 - Memory in the Subject of Computer Organization and Architecture

- Memory is a crucial component of a computer system that stores data and instructions for processing.
- Memory can be classified into different types and levels based on various factors such as capacity, access time, cost, and performance.
- Memory hierarchy is a concept that organizes memory into different levels, such that the higher levels have smaller capacity, faster access time, higher cost, and better performance than the lower levels.
- The main types of memory in a computer system are:

  - Register: The fastest and most expensive type of memory that is located inside the CPU and holds data and instructions that are currently being executed.
  - Cache: A small and fast type of memory that is located between the CPU and the main memory and holds frequently accessed data and instructions to reduce the average access time.
  - Main memory: A large and relatively slow type of memory that is directly accessible by the CPU and holds data and instructions that are currently in use by the programs.
  - Auxiliary memory: The largest and slowest type of memory that is external to the CPU and holds data and instructions that are not currently in use by the programs.

- Some of the design issues and performance factors that affect memory are:

  - Addressing: The method of identifying and locating data and instructions in memory. There are different types of addressing schemes such as direct, indirect, indexed, relative, etc.
  - Mapping: The method of assigning addresses to the physical locations of data and instructions in memory. There are different types of mapping techniques such as direct, associative, set-associative, etc.
  - Replacement: The method of choosing which data and instructions to remove from memory when there is no space available for new ones. There are different types of replacement policies such as least recently used (LRU), first in first out (FIFO), random, etc.
  - Write policy: The method of updating data and instructions in memory when they are modified by the CPU. There are two main types of write policies: write-through and write-back.
  - Locality: The principle that states that data and instructions that are accessed once are likely to be accessed again soon. There are two types of locality: temporal and spatial.
  - Hit ratio: The ratio of the number of successful accesses to memory to the total number of accesses. A higher hit ratio indicates better performance of memory.
  - Miss penalty: The additional time required to access memory when the requested data or instruction is not found in the desired level. A lower miss penalty indicates better performance of memory.