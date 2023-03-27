## Unit 2 - Distributed Mutual Exclusion

Distributed Mutual Exclusion is a fundamental problem in distributed computing where multiple processes try to access shared resources concurrently. The goal is to ensure that no two processes access the same resource at the same time and that all processes eventually gain access to the resource.

In this unit, we will learn about the different techniques and algorithms for achieving distributed mutual exclusion. The following are the key points that we will explore in this unit:

1. **Centralized Approaches:** In this approach, there is a central server that manages access to the shared resource. The server maintains a queue of requests and grants access to the resource to one process at a time. Examples of centralized approaches are Lamport's Algorithm and Ricart-Agrawala Algorithm.

2. **Distributed Approaches:** In this approach, there is no central server, and each process collaborates with other processes to manage access to the shared resource. Examples of distributed approaches are Maekawa's Algorithm and Suzuki-Kasami Algorithm.

3. **Token-Based Approaches:** In this approach, a token is passed from one process to another, and only the process holding the token can access the shared resource. Examples of token-based approaches are Chandy-Lamport Algorithm and Siva-Ramaswamy Algorithm.

4. **Quorum-Based Approaches:** In this approach, each process maintains a set of processes called a quorum, and a process can access the shared resource only if its quorum intersects with the quorum of the current holder of the resource. Examples of quorum-based approaches are Quorum-Based Mutual Exclusion and Hierarchical Quorum-Based Mutual Exclusion.

5. **Performance Metrics:** In addition to correctness, we also need to consider performance metrics such as message complexity, response time, and throughput when evaluating different distributed mutual exclusion algorithms.

6. **Challenges:** The main challenge in achieving distributed mutual exclusion is to ensure that the algorithm is correct and efficient under different conditions, such as process failures, message delays, and network partitions.

By the end of this unit, you will have a good understanding of the different approaches and techniques for achieving distributed mutual exclusion in distributed systems. You will also learn how to evaluate the performance of different algorithms and overcome the challenges involved in distributed mutual exclusion.