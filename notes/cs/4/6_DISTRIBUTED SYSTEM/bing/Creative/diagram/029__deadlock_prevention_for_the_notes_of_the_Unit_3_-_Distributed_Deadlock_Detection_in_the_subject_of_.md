According to the web search results, there are two ways to prevent deadlock in a distributed system: ordered request and collective request. The following diagram illustrates the basic architecture of a distributed system with deadlock prevention using ordered request method:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Process P1     |     |  Process P2     |     |  Process P3     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       V                     V                     V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Resource R1    |     |  Resource R2    |     |  Resource R3    |
|  Level 1        |     |  Level 2        |     |  Level 3        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

In this diagram, each resource type is assigned a certain level to maintain a resource request policy for a process. A process can only request resources higher than the highest level resources it currently holds. For example, if P1 holds R1, it can only request R2 or R3, but not R1 again. This method prevents the circular wait condition, which is one of the necessary conditions for deadlock. 

The following diagram illustrates the basic architecture of a distributed system with deadlock prevention using collective request method:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Process P1     |     |  Process P2     |     |  Process P3     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       V                     V                     V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Resource R1    |     |  Resource R2    |     |  Resource R3    |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

In this diagram, each process requests for all the required resources before the start of its execution. This prevents the hold and wait condition, which is another necessary condition for deadlock. This method may lead to low device utilization or starvation.