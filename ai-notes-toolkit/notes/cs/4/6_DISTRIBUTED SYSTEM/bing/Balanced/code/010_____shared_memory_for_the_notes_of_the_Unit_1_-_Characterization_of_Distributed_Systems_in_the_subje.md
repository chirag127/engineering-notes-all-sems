### Shared Memory

Shared memory is a memory architecture where physically separated memories can be addressed as a single shared address space. It allows multiple processes to access and modify the same data without explicit message passing.

Shared memory can be implemented in two ways:

- **Physical shared memory**: The memory is physically shared among multiple processors or nodes. This requires hardware support such as cache coherence circuits and network interface controllers. Examples of physical shared memory systems are symmetric multiprocessors (SMPs) and non-uniform memory access (NUMA) machines.
- **Distributed shared memory (DSM)**: The memory is physically distributed among multiple processors or nodes, but it is logically shared by using software techniques. The DSM system manages the memory across all the nodes and provides a virtual address space that is shared by all the nodes. The data moves between the main memories of different nodes as needed. Examples of DSM systems are Ivy, Munin, and TreadMarks.

The advantages of shared memory are:

- It simplifies the programming model by providing a single address space and a familiar memory abstraction.
- It allows the programmers to handle synchronizations in the familiar shared memory model using locks, semaphores, or monitors.
- It can improve the performance by reducing the communication overhead and exploiting the locality of data access.

The disadvantages of shared memory are:

- It can introduce consistency and coherence issues due to concurrent access and modification of the same data by multiple processes.
- It can increase the complexity of the system by requiring hardware or software mechanisms to maintain the consistency and coherence of the shared memory.
- It can limit the scalability of the system by imposing a fixed size of the shared memory or increasing the communication cost as the number of nodes increases.