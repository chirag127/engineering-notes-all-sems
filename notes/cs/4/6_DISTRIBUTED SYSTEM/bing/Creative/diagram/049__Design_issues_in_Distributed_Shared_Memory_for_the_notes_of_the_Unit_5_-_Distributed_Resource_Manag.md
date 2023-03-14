The following diagram illustrates the basic architecture of a distributed shared memory system:

```
+-----------------+     +-----------------+     +-----------------+
| Node 1          |     | Node 2          |     | Node 3          |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Application | |     | | Application | |     | | Application | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | DSM Library | |     | | DSM Library | |     | | DSM Library | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Local Cache | |     | | Local Cache | |     | | Local Cache | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+
                      |         |
                      |         |
                      v         v
                +-----------------+
                | Shared Memory  |
                | Server          |
                | +-------------+ |
                | | Data Blocks | |
                | +-------------+ |
                +-----------------+
```

The diagram shows the following components:

- Nodes: These are the machines that participate in the distributed system. Each node has its own local memory and runs an application that uses the DSM system.
- DSM Library: This is the software layer that provides the abstraction of a shared memory space to the application. It handles the communication, synchronization, and consistency protocols among the nodes.
- Local Cache: This is the memory region that stores the data blocks that are accessed by the application. It acts as a buffer between the local memory and the shared memory server.
- Shared Memory Server: This is the central repository that stores the data blocks that are shared by the nodes. It responds to the requests from the DSM library to read or write data blocks.