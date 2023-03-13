A distributed system is a system that consists of multiple independent components that communicate with each other over a network. A distributed system has some advantages, such as scalability, reliability, and performance, but also some limitations, such as the absence of a global clock and a shared memory.

The absence of a global clock means that there is no single source of time synchronization for all the components in the system. This makes it difficult to coordinate actions and order events across the system. For example, if two components want to update the same data, they need to agree on which update happened first, but without a global clock, they may have different views of time.

The absence of a shared memory means that there is no common storage space for all the components in the system. This makes it difficult to share data and state across the system. For example, if one component wants to read the data that another component has written, they need to communicate over the network, which may introduce delays, errors, or inconsistencies.

The following diagram illustrates the basic architecture of a distributed system using ASCII art:

```
+-----------------+     +-----------------+     +-----------------+
| Component 1     |     | Component 2     |     | Component 3     |
|                 |     |                 |     |                 |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Application | |     | | Application | |     | | Application | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Data        | |     | | Data        | |     | | Data        | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
+-----------------+     +-----------------+     +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +-----------------------+-----------------------+
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |