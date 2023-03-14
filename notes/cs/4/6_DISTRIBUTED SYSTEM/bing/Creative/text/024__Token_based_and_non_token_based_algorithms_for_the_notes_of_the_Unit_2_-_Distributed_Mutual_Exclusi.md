### Token based and non token based algorithms for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

Distributed mutual exclusion is the problem of ensuring that no two processes running on different nodes in a distributed system can access the same shared resource (such as a file, a database, or a critical section of code) at the same time. This is important to avoid inconsistency, deadlock, or corruption of data in the system.

There are two main approaches to solve the distributed mutual exclusion problem: token based and non token based algorithms.

#### Token based algorithms

In token based algorithms, a unique token is shared among all the nodes in the distributed system. The token acts as a permission to enter the critical section. A node can access the shared resource only if it has the token. The token is passed from one node to another according to some protocol, such as a logical ring, a tree, or a queue. The node that has the token can either use it to enter the critical section, or forward it to another node that has requested it.

Some advantages of token based algorithms are:

- They are free from deadlock, since there is always a unique token in the system that can break any cycle of waiting nodes.
- They ensure fairness, since the requests are executed in the order they are made or received by the token.
- They produce less message traffic, since only one token is circulated in the system.

Some disadvantages of token based algorithms are:

- They are prone to token loss or duplication, due to node or link failures, which can compromise the mutual exclusion property or cause starvation.
- They have high latency, since a node may have to wait for a long time to receive the token from another node that is far away or busy.
- They are not adaptive, since the token circulation pattern does not change according to the workload or the network topology.

Some examples of token based algorithms are:

- Suzuki-Kasami algorithm: This is a ring-based algorithm, where the token is passed along a logical ring of nodes. The token contains a vector of requests, where each entry indicates the highest request number received from each node. A node can enter the critical section only if its request number matches the entry in the token. When a node receives the token, it updates the vector with its own request number, and forwards the token to the next node in the ring that has a higher request number than the entry in the token.
- Raymond's algorithm: This is a tree-based algorithm, where the token is passed along a logical tree of nodes. The token is initially held by the root of the tree. A node can enter the critical section only if it has the token. When a node requests the token, it sends a REQUEST message to its parent in the tree. The parent either grants the token to the node, or forwards the request to its parent, and so on. When a node receives the token, it becomes the new root of the tree, and can grant the token to its children. The tree structure changes dynamically according to the requests.

#### Non token based algorithms

In non token based algorithms, also known as permission based algorithms, there is no token in the system. Instead, a node communicates with a set of other nodes to obtain their permission to enter the critical section. The permission is granted by sending a REPLY message to the requesting node. A node can access the shared resource only if it has received REPLY messages from all the nodes in the set.

Some advantages of non token based algorithms are:

- They are resilient to node or link failures, since there is no token to be lost or duplicated.
- They have low latency, since a node can enter the critical section as soon as it receives all the REPLY messages, without waiting for a token to arrive.
- They are adaptive, since the communication pattern can change according to the workload or the network topology.

Some disadvantages of non token based algorithms are:

- They are susceptible to deadlock, since there may be cycles of waiting nodes that cannot grant permission to each other.
- They do not ensure fairness, since the requests are executed according to the arrival of REPLY messages, which may not reflect the order of requests.
- They produce more message traffic, since multiple rounds of messages are exchanged for each request.

Some examples of non token based algorithms are:

- Ricart-Agrawala algorithm: This is a quorum-based algorithm, where the set of nodes that grant permission is the entire system. A node can enter the critical section only if it has received REPLY messages from all the other nodes in the system. When a node requests the critical