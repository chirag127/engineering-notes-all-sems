## Unit 2 - Distributed Mutual Exclusion

In a distributed system, multiple processes running on different nodes may require access to a shared resource simultaneously. Distributed Mutual Exclusion (DME) is a technique used to ensure that only one process at a time can access the shared resource.

### Centralized Approach

A centralized approach to mutual exclusion involves a single node (usually a server) that controls access to the shared resource. Whenever a process needs access to the resource, it sends a request to the server. The server then grants access to the resource to the requesting process and informs all other processes that the resource is currently in use.

#### Advantages

- Simple to implement
- Easy to understand

#### Disadvantages

- Single point of failure
- Bottleneck for high traffic systems
- Increases latency due to network communication

### Decentralized Approach

A decentralized approach to mutual exclusion involves multiple nodes working together to ensure that only one process at a time can access the shared resource. There are several algorithms for achieving DME, including token-based algorithms and election-based algorithms.

#### Token-Based Algorithms

Token-based algorithms use a token (a special message or object) that is passed between processes to control access to the shared resource. Only the process holding the token can access the resource. When a process is done using the resource, it passes the token to the next process in a predetermined order.

##### Advantages

- Simple to understand and implement
- Low overhead

##### Disadvantages

- Token overhead may increase with the number of nodes
- Token loss may cause deadlock or livelock

#### Election-Based Algorithms

Election-based algorithms use a leader election process to determine which process has access to the shared resource. The leader is responsible for granting access to the resource to other processes. When a process needs access to the resource, it sends a request to the leader. The leader then grants access to the resource to the requesting process.

##### Advantages

- No single point of failure
- Scalable for large systems

##### Disadvantages

- Leader election may cause overhead
- Complexity increases with the number of nodes

### Learning Tricks

- Remember the acronym "DME" as "Don't Make Errors". This can help remind you that DME is used to prevent errors and conflicts in a distributed system.