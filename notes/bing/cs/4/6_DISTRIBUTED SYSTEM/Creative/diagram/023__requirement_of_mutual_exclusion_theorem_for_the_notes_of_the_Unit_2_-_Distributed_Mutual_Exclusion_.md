The requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM is as follows:

Mutual exclusion is a program object that refers to the requirement of satisfying that no two concurrent processes are in a critical section at the same time. It is presented to intercept the race condition. If a current process is accessing the critical section then it prevents entering another concurrent process there.

A critical section is a piece of code that accesses shared resources (such as data structures, files, devices, etc.) that must not be accessed by more than one process at a time.

A distributed system is a collection of independent computers that communicate with each other over a network. A distributed mutual exclusion algorithm is a protocol that ensures that only one process in the distributed system can execute the critical section at a time.

A distributed mutual exclusion algorithm must satisfy the following requirements:

- No deadlock: Two or more sites should not endlessly wait for any message that will never arrive.
- No starvation: Every site who wants to execute critical section should get an opportunity to execute it in finite time.
- Fairness: Each site should get a fair chance to execute the critical section according to some ordering policy.
- Fault tolerance: The algorithm should be able to handle the failure of some sites or communication links without affecting the correctness of the algorithm.

The following diagram illustrates the basic architecture of a distributed system with mutual exclusion:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Process 1    |       |    Process 2    |       |    Process 3    |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Critical       |       |  Critical       |       |  Critical       |
|  Section        |       |  Section        |       |  Section        |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Mutual         |       |  Mutual         |       |  Mutual         |
|  Exclusion      |       |  Exclusion      |       |  Exclusion      |
|  Algorithm      |       |  Algorithm      |       |  Algorithm      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Communication  |       |  Communication  |       |  Communication  |
|  Module         |       |  Module         |       |  Module         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
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