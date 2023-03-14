## Unit 2 - Consensus

A consensus algorithm is a process in computer science used to achieve agreement on a single data value among distributed processes or systems. These algorithms are designed to achieve reliability in a network involving multiple users or nodes. Consensus algorithms are important in distributed computing and multi-agent systems such as those seen in cryptocurrency blockchain networks.

The following diagram illustrates the basic architecture of a consensus algorithm:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Process 1    |     |    Process 2    |     |    Process 3    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Consensus      |     |  Consensus      |     |  Consensus      |
|  Algorithm      |     |  Algorithm      |     |  Algorithm      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+
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
+-----------------+
|                 |
|  Consensus      |
|  Value          |
|                 |
+-----------------+
```

The diagram shows three processes that are part of a distributed system. Each process has its own consensus algorithm that communicates with the other processes to reach an agreement on a single data value. The consensus value is the result of the consensus algorithm and represents the state of the system. The consensus algorithm must ensure that the consensus value is consistent, reliable, and fault-tolerant.