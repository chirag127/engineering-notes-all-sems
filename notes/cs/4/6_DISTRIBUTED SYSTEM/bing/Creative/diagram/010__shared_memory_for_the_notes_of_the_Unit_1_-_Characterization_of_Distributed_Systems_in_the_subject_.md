### Shared memory for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

Shared memory is a form of memory architecture where physically separated memories can be addressed as a single shared address space. The term "shared" does not mean that there is a single centralized memory, but that the address space is shared—i.e., the same physical address on two processors refers to the same location in memory.

A distributed shared memory (DSM) system is a collection of many nodes/computers which are connected through some network and all have their local memories. The DSM system manages the memory across all the nodes. All the nodes/computers transparently interconnect and process.

The following diagram illustrates the basic architecture of a DSM system:

```
    +-----------------+      +-----------------+      +-----------------+
    | Node 1          |      | Node 2          |      | Node 3          |
    | +-------------+ |      | +-------------+ |      | +-------------+ |
    | | CPU         | |      | | CPU         | |      | | CPU         | |
    | +-------------+ |      | +-------------+ |      | +-------------+ |
    | | Memory      | |      | | Memory      | |      | | Memory      | |
    | | +---------+ | |      | | +---------+ | |      | | +---------+ | |
    | | | Block A | | |      | | | Block B | | |      | | | Block C | | |
    | | +---------+ | |      | | +---------+ | |      | | +---------+ | |
    | | | Block D | | |      | | | Block E | | |      | | | Block F | | |
    | | +---------+ | |      | | +---------+ | |      | | +---------+ | |
    | | | Block G | | |      | | | Block H | | |      | | | Block I | | |
    | | +---------+ | |      | | +---------+ | |      | | +---------+ | |
    | +-------------+ |      | +-------------+ |      | +-------------+ |
    +-----------------+      +-----------------+      +-----------------+
          |  |  |                |  |  |                |  |  |
          |  |  +----------------+  |  +----------------+  |  |
          |  +---------------------+  +---------------------+  |
          +----------------------------------------------------+
                           Communication Network
```

Each node consists of one or more CPUs and a memory unit. A high-speed communication network is used for connecting the nodes. A simple message passing system allows processes on different nodes to exchange messages.

Memory mapping manager unit:

Memory mapping manager routine in each node maps the local memory onto the shared memory space. For mapping operation, the shared memory space is divided into blocks. Data caching is a well-known solution to address operation latency. DSM uses data caching to reduce network latency. The main memory of the individual nodes is used to cache pieces of the shared memory space. Memory mapping manager of each node reads its local memory as a big cache of the shared memory space for its associated processors. The base unit of caching is a memory block. Systems that support DSM, data moves between secondary memory and main memory as well as between main memories of different nodes. Each DSM object is owned by a node. The initial owner is the node that created the object. Ownership can change as the object moves from node to node. When a process accesses data in the shared address space, the mapping manager maps shared memory address to physical memory (local or remote).

Communication Network Unit:

When a process accesses data in the shared address space, the mapping manager maps the shared memory address to the physical memory. The mapped layer of software implemented either in the operating system kernel or as a runtime library.

Advantages of DSM:

- Scales well with a large number of nodes
- Message passing is hidden
- Can handle complex and large databases without replication or sending the data to processes
- Generally cheaper than using a multiprocessor system
- Provides large virtual memory space
- Programs are more portable due to common programming interfaces
- Shield programmers from sending or receiving primitives

Disadvantages of DSM:

- Generally slower to access than non-distributed shared memory
- Must provide additional protection against simultaneous accesses to shared data
- May incur a performance