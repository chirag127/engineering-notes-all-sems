# Shared Memory

- Shared memory is a method of inter-process communication (IPC) that allows multiple processes to access a common region of memory.
- Shared memory can be used for data exchange, synchronization, or coordination among processes.
- Shared memory is faster than other IPC methods, such as message passing or pipes, because it avoids the overhead of copying data between processes or kernel space.
- Shared memory can be implemented in different ways, depending on the hardware and software architecture of the system.

## Shared Memory Systems

- A shared memory system is a computer system that has a pool of processors (P1, P2, etc.) that can read and write a collection of memories (M1, M2, etc.).
- A shared memory system can be classified into two types: uniform memory access (UMA) and non-uniform memory access (NUMA).
- In a UMA system, all the processors have equal access to all the memories, and the access time is the same for any memory location. UMA systems are typically implemented with a single bus or a crossbar switch that connects all the processors and memories.
- In a NUMA system, each processor has a direct connection to a block of main memory, and the processors can access each others’ blocks of main memory through special hardware or software. NUMA systems are typically implemented with multiple buses or a network of interconnects that link the processors and memories.
- UMA systems are simpler and more scalable than NUMA systems, but they suffer from contention and latency issues when the number of processors or the memory size increases.
- NUMA systems can provide higher performance and lower power consumption than UMA systems, but they require more complex hardware and software support for memory management and coherence.

## Shared Memory in Embedded Systems

- Embedded systems are specialized computer systems that are designed for specific applications, such as control, communication, or sensing.
- Embedded systems often have limited resources, such as memory, power, or processing speed, and they need to meet real-time constraints, such as deadlines, throughput, or reliability.
- Shared memory can be used in embedded systems to facilitate data exchange and synchronization among multiple tasks or processes that run on the same or different processors.
- Shared memory can also be used to implement distributed shared memory (DSM) for embedded systems that have multiple processors connected by a network. DSM provides location-transparent shared variables, so that distributed software modules can exchange their input and output values through shared variables on DSM.
- Shared memory in embedded systems can be implemented using hardware or software techniques, or a combination of both.
- Hardware techniques include using dedicated memory chips, memory-mapped I/O devices, or on-chip memory blocks that can be accessed by multiple processors or cores.
- Software techniques include using operating system services, libraries, or middleware that provide shared memory abstraction and management for the applications.
- Hardware techniques are faster and more reliable than software techniques, but they are more expensive and less flexible.
- Software techniques are cheaper and more adaptable than hardware techniques, but they introduce more overhead and complexity.