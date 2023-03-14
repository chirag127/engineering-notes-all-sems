### Token based and non token based algorithms for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

Distributed Mutual Exclusion is a mechanism that ensures that only one process at a time accesses a shared resource in a distributed system. There are two types of algorithms used for Distributed Mutual Exclusion, token-based and non-token-based algorithms.

#### Token-based Algorithm

A token-based algorithm is a distributed algorithm that uses a token to control the access to a shared resource in a distributed system. The token is passed from one process to another, and only the process that holds the token can access the shared resource.

##### Advantages

- The token-based algorithm provides a guaranteed order of access to the shared resource.
- It is easy to implement and use.
- There is no need for frequent communication between processes, which reduces network traffic.

##### Disadvantages

- The token-based algorithm can introduce delays if a process holds the token for a long time.
- The token-based algorithm may not be suitable for systems with a large number of processes.

##### Example

The Ricart-Agrawala algorithm is an example of a token-based algorithm.

#### Non-Token-based Algorithm

A non-token-based algorithm is a distributed algorithm that does not use a token to control the access to a shared resource in a distributed system. In this algorithm, each process requests access to the shared resource and waits for a reply from other processes before accessing the resource.

##### Advantages

- The non-token-based algorithm can handle a large number of processes and shared resources.
- It can be used in systems where there is no guarantee of a reliable network.

##### Disadvantages

- The non-token-based algorithm may introduce delays if there are a large number of requests for access to the shared resource.
- It is more complex to implement than the token-based algorithm.

##### Example

The Lamport's algorithm is an example of a non-token-based algorithm.

#### Learning Trick

To remember the difference between token-based and non-token-based algorithms, think of it as a queue at a grocery store. In the token-based algorithm, only the person holding the token can access the cashier, while in the non-token-based algorithm, everyone has to wait in line and take turns accessing the cashier.