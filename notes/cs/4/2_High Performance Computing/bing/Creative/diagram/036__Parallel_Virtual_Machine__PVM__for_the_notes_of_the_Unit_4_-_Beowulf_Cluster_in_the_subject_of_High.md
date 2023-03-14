Parallel Virtual Machine (PVM) is a software tool for parallel networking of computers. It is designed to allow a network of heterogeneous Unix and/or Windows machines to be used as a single distributed parallel processor. 

The following diagram illustrates the basic architecture of a PVM system:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  PVM daemon     |     |  PVM daemon     |     |  PVM daemon     |
|  (pvmd)         |     |  (pvmd)         |     |  (pvmd)         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  PVM tasks      |     |  PVM tasks      |     |  PVM tasks      |
|  (user programs)|     |  (user programs)|     |  (user programs)|
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Operating      |     |  Operating      |     |  Operating      |
|  system         |     |  system         |     |  system         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Hardware       |     |  Hardware       |     |  Hardware       |
|  (CPU, memory,  |     |  (CPU, memory,  |     |  (CPU, memory,  |
|  disk, network) |     |  disk, network) |     |  disk, network) |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                   |                   |
       |                   |                   |
       +-------------------+-------------------+
                           |
                           |
                      +----+----+
                      |         |
                      |  Network|
                      |         |
                      +----+----+
                           |
                           |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  PVM daemon     |     |  PVM daemon     |     |  PVM daemon     |
|  (pvmd)         |     |  (pvmd)         |     |  (pvmd)         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  PVM tasks      |     |  PVM tasks      |     |  PVM tasks      |
|  (user programs)|     |  (user programs)|     |  (user programs)|
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Operating      |     |  Operating      |     |  Operating      |
|  system         |     |  system         |     |  system         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Hardware       |     |  Hardware       |     |  Hardware       |
|  (CPU, memory,  |     |  (CPU, memory,  |     |  (CPU, memory,  |
|  disk, network) |     |  disk, network) |     |  disk, network) |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

Each machine in the network runs a PVM daemon (pvmd) that is responsible for communication, task management, and fault detection. The user programs (PVM tasks) can be started on any machine and can communicate with each other using message-passing routines provided by the PVM library. The network can be any combination of Ethernet, FDDI, or other interconnection technologies.