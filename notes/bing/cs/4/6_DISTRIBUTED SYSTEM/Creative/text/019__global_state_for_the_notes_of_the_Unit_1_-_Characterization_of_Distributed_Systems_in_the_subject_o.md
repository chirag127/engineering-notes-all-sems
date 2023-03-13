### Global State

- A global state of a distributed system is a collection of local states of all the processes and the messages in transit at a given instant.
- A global state can be used to detect global properties of a distributed system, such as deadlock, termination, consistency, etc.
- A global state can be represented by a global state vector, which is a vector of local state vectors, one for each process.
- A local state vector of a process consists of its local variables, program counter, and the messages it has sent and received.
- A global state vector can be obtained by taking a consistent snapshot of the distributed system, which is a set of local states that reflects a possible global state.
- A snapshot is consistent if it satisfies the happened-before relation, which is a partial order that defines the causal dependencies between events in a distributed system.
- The happened-before relation states that if event a happens before event b in the same process, then a -> b, and if event a is the sending of a message and event b is the receiving of that message, then a -> b.
- A snapshot is inconsistent if it violates the happened-before relation, such as showing a message as received but not sent, or showing a message as sent but not received.
- A consistent snapshot can be taken using various algorithms, such as Chandy-Lamport, Lai-Yang, etc.