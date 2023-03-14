The following diagram illustrates the basic architecture of a high-performance grid using ASCII characters. The grid consists of a grid kernel that provides uniform resource management services and runs on both network equipment and host computers. The grid kernel communicates with grid services that are layered on top of it and provide more comprehensive functionality. The grid services can access the grid resources, such as compute nodes, storage nodes, and network devices, through the grid kernel. The grid users can interact with the grid services through a grid portal or a grid application.

```
+-----------------+     +-----------------+     +-----------------+
| Grid Portal     |     | Grid Application|     | Grid Service    |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
| Grid Service    |     | Grid Service    |     | Grid Service    |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
| Grid Kernel     |     | Grid Kernel     |     | Grid Kernel     |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
| Grid Resource   |     | Grid Resource   |     | Grid Resource   |
+-----------------+     +-----------------+     +-----------------+
```