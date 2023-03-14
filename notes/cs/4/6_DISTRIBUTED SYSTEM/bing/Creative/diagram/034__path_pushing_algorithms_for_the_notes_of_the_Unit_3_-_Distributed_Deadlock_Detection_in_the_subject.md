Path-pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG). The main idea is to create a global WFG for each site of the distributed system. When a site in this class of algorithms performs a deadlock computation, it sends its local WFG to all neighboring sites. The neighboring sites then merge their local WFGs with the received WFG and send the updated WFG to their neighbors. This process continues until all sites have the same global WFG. Then, each site can check for cycles in the global WFG to detect deadlocks .

The following diagram illustrates the basic architecture of a path-pushing algorithm:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|     Site 1      |      |     Site 2      |      |     Site 3      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Local WFG 1    |      |  Local WFG 2    |      |  Local WFG 3    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| Deadlock        |      | Deadlock        |      | Deadlock        |
| Computation     |      | Computation     |      | Computation     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Send/Receive   |<---->|  Send/Receive   |<---->|  Send/Receive   |
|  WFG            |----->|  WFG            |----->|  WFG            |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```