The following diagram illustrates the basic architecture of a distributed shared memory system using the central server algorithm . The central server maintains all the shared data and services the read and write requests from the nodes. The nodes communicate with the server using messages and receive acknowledgements or data in return.

```
+-----------------+       +-----------------+
|                 |       |                 |
|     Node 1      |       |     Node 2      |
|                 |       |                 |
+-----------------+       +-----------------+
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
+-----------------+       +-----------------+
|                 |       |                 |
|     Node 3      |       |     Node 4      |
|                 |       |                 |
+-----------------+       +-----------------+
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       |                         |
       +-------------------------+
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
+-----------------+
|                 |
|  Central Server |
|                 |
+-----------------+
```