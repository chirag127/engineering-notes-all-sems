### Edge Chasing Algorithms

Edge chasing algorithms are used for distributed deadlock detection in distributed systems. Here are some key points to note about edge chasing algorithms:

1. Edge chasing algorithms are based on the concept of sending probe messages to detect cycles in the wait-for graph.
2. A probe message contains information about the initiator of the probe, the current transaction, and the dependent transaction.
3. When a transaction receives a probe message, it checks if it is waiting for any other transaction. If it is, it forwards the probe message to the transaction it is waiting for.
4. If a transaction receives a probe message that it has initiated, it means that a cycle has been detected and a deadlock has occurred.
5. Edge chasing algorithms can be classified into two types: the basic edge chasing algorithm and the diffusing computation edge chasing algorithm.
6. The basic edge chasing algorithm is simple to implement but can generate a large number of probe messages.
7. The diffusing computation edge chasing algorithm is more efficient as it reduces the number of probe messages generated.

This is a brief overview of edge chasing algorithms for distributed deadlock detection in distributed systems. It is important to understand these algorithms in order to effectively detect and resolve deadlocks in distributed systems.