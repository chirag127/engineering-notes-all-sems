### Token based and non-token based algorithms for the notes of Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

Distributed Mutual Exclusion is a crucial concept in Distributed Systems, which ensures that multiple processes in a distributed system do not access the same resource simultaneously. In this unit, we will discuss two types of algorithms to achieve Mutual Exclusion - Token-based and Non-token based algorithms.

#### Token-based algorithms

Token-based algorithms use a special token that is passed among the processes in a distributed system to determine which process can access a shared resource at a given point in time. The following are the types of Token-based algorithms:

1. **Centralized Token-based Algorithm:** In this algorithm, there is a central authority that controls the access to shared resources. Only the process that holds the token can access the shared resource. This algorithm is simple to implement, but it has a single point of failure.

2. **Distributed Token-based Algorithm:** In this algorithm, the token is passed among the processes in a distributed system. The process that holds the token can access the shared resource. This algorithm is fault-tolerant, but it may lead to starvation if a process never gets the token.

#### Non-token based algorithms

Non-token-based algorithms do not use a special token to determine which process can access a shared resource. Instead, they use a set of rules to determine which process can access the shared resource at a given point in time. The following are the types of Non-token based algorithms:

1. **Timestamp-based Algorithm:** In this algorithm, each process is assigned a unique timestamp value. The process with the lowest timestamp value can access the shared resource. This algorithm is simple to implement, but it may lead to starvation if a process has a higher timestamp value than the other processes.

2. **Quorum-based Algorithm:** In this algorithm, a quorum of processes is required to access the shared resource. The quorum is a subset of processes that must agree to access the shared resource. This algorithm is fault-tolerant and avoids starvation, but it may lead to a deadlock if the quorum cannot be formed.

In conclusion, both Token-based and Non-token based algorithms are used to achieve Mutual Exclusion in a distributed system. The choice of algorithm depends on the specific requirements of the system, such as fault-tolerance, simplicity, and avoidance of starvation or deadlock.