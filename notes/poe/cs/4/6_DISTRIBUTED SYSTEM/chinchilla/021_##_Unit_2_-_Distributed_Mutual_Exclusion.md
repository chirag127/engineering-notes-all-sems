## Unit 2 - Distributed Mutual Exclusion

Distributed mutual exclusion is the process of coordinating access to a shared resource in a distributed system, where multiple processes or nodes need to access the resource simultaneously. The goal is to ensure that only one process at a time can access the shared resource, to prevent conflicts and ensure consistency.

### Centralized Approaches

Centralized approaches are based on having a single node, known as the coordinator, responsible for managing access to the shared resource. The coordinator maintains a queue of requests from nodes and grants access to the shared resource to one node at a time, based on a predefined policy.

#### Advantages
- Simple to implement and understand
- Can be efficient for small systems with a low number of nodes

#### Disadvantages
- Single point of failure
- Scalability issues as the number of nodes increases
- Coordinator can become a bottleneck

### Decentralized Approaches

Decentralized approaches distribute the responsibility of managing access to the shared resource among the nodes in the system. Nodes collaborate to ensure that only one node at a time can access the resource, without the need for a central coordinator.

#### Token-Based Algorithms

Token-based algorithms use a token, which is passed from node to node in a predetermined order. The node holding the token has the right to access the shared resource, while other nodes must wait until the token is passed to them.

##### Advantages
- No need for a central coordinator
- Guaranteed fairness, as each node receives the token in a predetermined order

##### Disadvantages
- One node may hold the token for an extended period, causing delays for other nodes
- Token can become a bottleneck in high-traffic systems

#### Distributed Queuing Algorithms

Distributed queuing algorithms maintain a local queue of requests at each node, which are forwarded to other nodes in a predetermined order. The node at the head of the queue has the right to access the shared resource, while other nodes must wait until their request reaches the head of the queue.

##### Advantages
- No need for a central coordinator
- No single point of failure
- Scalable and efficient for large systems

##### Disadvantages
- May lead to starvation, where some nodes never get access to the shared resource
- More complex to implement than token-based algorithms

### Learning Trick

Remember the phrase "Distribute the power, avoid the bottleneck" to recall the advantages of decentralized approaches and the disadvantages of centralized approaches in distributed mutual exclusion.