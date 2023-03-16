### Edge Chasing Algorithms

Edge chasing algorithms are used for distributed deadlock detection in distributed systems. Here are some key points to note about edge chasing algorithms:

1. Edge chasing algorithms are based on the concept of sending probe messages to detect cycles in the wait-for graph.
2. A probe message contains information about the initiator of the probe, the current transaction, and the dependent transaction.
3. When a transaction receives a probe message, it checks if it is waiting for any other transaction. If it is, it forwards the probe message to the transaction it is waiting for.
4. If a transaction receives a probe message that contains its own identifier, it means that a cycle has been detected and a deadlock has occurred.
5. Edge chasing algorithms can be classified into two categories: diffusing computation and centralized control.
6. In diffusing computation, each transaction is responsible for initiating a probe message when it detects that it is waiting for another transaction.
7. In centralized control, a single coordinator is responsible for initiating probe messages and detecting deadlocks.
8. Edge chasing algorithms can be used in both distributed and centralized systems.
