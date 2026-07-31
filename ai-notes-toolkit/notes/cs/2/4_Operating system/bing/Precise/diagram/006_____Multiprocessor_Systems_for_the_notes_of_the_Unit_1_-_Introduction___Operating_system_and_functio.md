### Multiprocessor Systems

Multiprocessor systems, also known as parallel systems or tightly-coupled systems, have two or more processors that are closely connected and share the computer's main memory and I/O facilities. These systems are designed to improve performance through parallelism, where multiple processors work together to execute multiple tasks simultaneously.

Here are some key points to remember about multiprocessor systems:

1. Multiprocessor systems can be classified into three categories: symmetric multiprocessing (SMP), asymmetric multiprocessing (ASMP), and NUMA (Non-Uniform Memory Access).
2. In SMP systems, all processors are treated as equals and share the same operating system. Each processor can perform any task, and the workload is distributed evenly among them.
3. In ASMP systems, each processor is assigned a specific task or role. One processor may act as the master, controlling the system and assigning tasks to other processors, while the others act as slaves, performing the tasks assigned to them.
4. In NUMA systems, memory access times vary depending on the location of the memory relative to the processor accessing it. This can result in improved performance for certain types of workloads.
5. Multiprocessor systems can improve performance by allowing multiple tasks to be executed simultaneously. However, the performance gains depend on the ability of the system to effectively distribute the workload among the processors.
6. The design and implementation of the operating system is critical in multiprocessor systems, as it must effectively manage the allocation of resources and the synchronization of tasks among the processors.
