### Causal Ordering of Messages for the Notes of Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

In a distributed system, messages are sent between different processes. It is important to ensure that the messages are delivered in the intended order, especially when the order of delivery affects the result of the computation. Causal ordering is a mechanism used to ensure that messages are delivered in a causally consistent order.

Causal ordering is based on the concept of happened-before relation. If event A happened before event B, then A causally depends on B. In a distributed system, happened-before relation can be established based on the following rules:

1. If event A and event B are in the same process, and A is executed before B, then A happened before B.
2. If event A is the sending of a message m and event B is the receipt of message m, then A happened before B.
3. If event A happened before event B and event B happened before event C, then A happened before C.

Based on these rules, we can establish the happened-before relation between events in a distributed system. Causal ordering ensures that messages are delivered in the causally consistent order. If message m1 causally depends on message m2, then m2 must be delivered before m1.

There are different algorithms for causal ordering, such as vector clocks and Lamport timestamps. Vector clocks assign a vector to each process, where the i-th element of the vector represents the number of events that have occurred in process i. Lamport timestamps assign a timestamp to each event, which is a pair (t, p), where t is a logical timestamp and p is the id of the process that generated the event.

Mnemonics and Learning Tricks:

1. Remember the rules for establishing happened-before relation: same process, sending and receipt of message, and transitivity.
2. Vector clocks assign a vector to each process, while Lamport timestamps assign a timestamp to each event.
3. Think of causally consistent order as a sequence of events that respect the happened-before relation.

In summary, causal ordering is a mechanism used to ensure that messages are delivered in a causally consistent order in a distributed system. It is based on the concept of happened-before relation, which can be established based on the rules of same process, sending and receipt of message, and transitivity. Vector clocks and Lamport timestamps are algorithms used for causal ordering. Remembering these rules and algorithms can be helpful in understanding and implementing causal ordering in distributed systems.