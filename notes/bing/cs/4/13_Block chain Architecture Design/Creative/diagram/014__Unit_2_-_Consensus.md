A consensus algorithm is a process in computer science used to achieve agreement on a single data value among distributed processes or systems. These algorithms are designed to achieve reliability in a network involving multiple users or nodes. Consensus algorithms are vital in large-scale, fault-tolerant systems because they enable a set of distributed/ replicated machines or servers to work as a coherent group and agree on system state, even in the presence of failures or outages.

There are different types of consensus algorithms, such as proof of work, proof of stake, practical Byzantine fault tolerance, HotStuff, etc  . Each of them has its own advantages and disadvantages in terms of security, performance, scalability, and resource consumption.

## Unit 2 - Consensus

The following diagram illustrates the basic architecture of a consensus algorithm in a distributed system:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Node 1       |     |    Node 2       |     |    Node 3       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Proposal     |     |    Proposal     |     |    Proposal     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Vote         |     |    Vote         |     |    Vote         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Decision     |     |    Decision     |     |    Decision     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       +--------------------+--------------------+
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |