### edge chasing algorithms for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

Edge chasing algorithms are a type of distributed deadlock detection algorithm used in distributed systems. The goal of these algorithms is to detect deadlocks in a distributed system, where multiple processes are executing concurrently on different nodes.

In edge chasing algorithms, each node in the system maintains information about the resources it holds and the resources it is waiting for. When a process requests a resource, it sends a request message to the node that holds the resource. The node that holds the resource then sends a reply message indicating whether the resource is available or not.

The edge chasing algorithm uses these request and reply messages to build a graph of the resource allocation and waiting relationships in the system. The algorithm then searches the graph for cycles, which indicate a deadlock.

Edge chasing algorithms are efficient in terms of communication overhead, as they only require messages to be exchanged between nodes when a resource request is made. However, they can be complex to implement and may not detect all deadlocks in a system.

It is important to have a deadlock detection mechanism in place in a distributed system to prevent processes from becoming stuck and to ensure the system remains responsive and available. Edge chasing algorithms are one approach to solving this problem, but other algorithms, such as timeout-based or global state detection algorithms, may also be used.
