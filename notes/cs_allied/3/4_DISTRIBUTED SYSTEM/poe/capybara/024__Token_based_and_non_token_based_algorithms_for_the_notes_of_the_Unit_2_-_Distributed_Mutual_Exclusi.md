### Token based and non token based algorithms for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

In distributed systems, mutual exclusion is a crucial concept that ensures that only one process at a time can access a shared resource. Two of the most commonly used algorithms for achieving mutual exclusion are token-based and non-token-based algorithms.

#### Token-based Algorithm

A token-based algorithm is a distributed mutual exclusion algorithm that uses a token to control access to a shared resource. The token is passed between the processes, and only the process that holds the token can access the shared resource. The steps involved in a token-based algorithm are as follows:

1. A process requests the token from the process that currently holds it.
2. The process that holds the token sends the token to the requesting process.
3. The requesting process accesses the shared resource.
4. After accessing the resource, the process releases the token and passes it to the next process in the token ring.

#### Non-token-based Algorithm

A non-token-based algorithm is a distributed mutual exclusion algorithm that does not use a token to control access to a shared resource. Instead, a process broadcasts a request message to all other processes in the system, and the process that has the right to access the shared resource responds to the request. The steps involved in a non-token-based algorithm are as follows:

1. A process broadcasts a request message to all other processes in the system.
2. The process that has the right to access the shared resource responds to the request.
3. The requesting process accesses the shared resource.
4. After accessing the resource, the process releases it, allowing other processes to access it.

#### Comparison

Token-based algorithms have the advantage of simplicity and speed, as they require only one message to be sent between processes. However, they can be less flexible than non-token-based algorithms, as the token must be passed sequentially between processes.

Non-token-based algorithms are more flexible, as any process can access the shared resource at any time. However, they require more messages to be sent between processes, which can lead to slower performance.

In conclusion, both token-based and non-token-based algorithms have their advantages and disadvantages, and the choice of which to use depends on the specific requirements of the distributed system.