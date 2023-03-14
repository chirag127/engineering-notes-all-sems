The following diagram illustrates the basic architecture of a centralized deadlock detection approach in a distributed system. It uses a central coordinator to manage a resource graph of processes and the resources they are using. The coordinator periodically checks the graph for cycles, which indicate deadlocks. If a deadlock is detected, the coordinator can initiate a recovery action, such as aborting one of the processes in the cycle.

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Site 1       |      |    Site 2       |      |    Site 3       |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Process 1    |      |    Process 2    |      |    Process 3    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Resource 1   |      |    Resource 2   |      |    Resource 3   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
      |  |                |  |                |  |
      |  +----------------+  |                |  |
      |     Request          |                |  |
      |                      |                |  |
      |                      |                |  |
      |                      |                |  |
      |                      |                |  |
      |                      |                |  |
      |                      |                |  |
      |                      |                |  |
      |                      |                |  |
      |                      |                |  |
      |                      |                |  |
      |                      |                |  |
      |                      |                |  |
      |                      |                |  |
      |                      |                |  |
      +----------------------+                |  |
         Request                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |
                                             |  |