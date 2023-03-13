Voting protocols are a technique for achieving fault tolerance in distributed systems, where a set of nodes have to agree on a common value or decision. Voting protocols can be classified into two types: exact and inexact. Exact voting protocols require that all nodes have the same value or decision, while inexact voting protocols allow some degree of variation or approximation.

A basic voting protocol consists of two phases: a voting phase and a decision phase. In the voting phase, each node sends its value or decision to a coordinator node, which collects all the votes and determines the outcome. In the decision phase, the coordinator node broadcasts the outcome to all the nodes, which update their state accordingly.

A possible ASCII diagram for a basic voting protocol is shown below:

```
    +-----+        +-----+        +-----+
    | N1  |        | N2  |        | N3  |
    +-----+        +-----+        +-----+
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       +------------->|              |
       |              +------------->|
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              +------------->|
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |<-------------+              |
       |              |<-------------+
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |<-------------+              |
       |              |<-------------+
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       +------------->|              |
       |              +------------->|
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              +------------->|
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
       |              |              |
    +-----+        +-----+        +-----+
    | N1  |        | N2  |        | N3  |
    +-----+        +-----+        +-----+
```

The diagram shows three nodes, N1, N2, and N3, participating in a voting protocol. The coordinator node is N1. The arrows indicate the messages exchanged between the nodes. The messages are:

- N1 -> N2: Request vote
- N2 -> N3: Request vote
- N3 -> N1: Send vote
- N2 -> N1: Send vote
- N1 -> N2: Send outcome
- N1 -> N3: Send outcome

The diagram assumes that there are no failures or attacks in the system. In reality, voting protocols have to deal with various types of faults and threats, such as node crashes, network partitions, message losses, message delays, message corruptions, message duplications, message reordering, malicious nodes, etc. To handle these situations, voting protocols have to use various techniques, such as timeouts, acknowledgments, encryption, signatures, authentication, etc. Different voting protocols may have different assumptions, requirements, and guarantees for fault tolerance and security. For more details, please refer to the sources     that I used to generate this response.