### Causal order for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Causal order is a partial order of messages in a distributed system that reflects the potential causal relationships between events.
- Causal order is based on the principle of Lamport's logical clocks, which assign a logical timestamp to each event in a distributed system.
- Causal order ensures that if an event e1 causally precedes an event e2, then the message carrying e1 is delivered before the message carrying e2 to any process that receives both messages.
- Causal order is useful for maintaining consistency and avoiding anomalies in distributed systems, such as seeing an answer before a question, or violating the happens-before relation.
- Causal order can be enforced by various algorithms, such as vector clocks, causal broadcast, or causal multicast .
- Causal order is weaker than total order, which imposes a global order on all messages in a distributed system, regardless of causality.
- Causal order is stronger than unordered or sync-ordered communication, which do not guarantee any ordering of messages in a distributed system.

Some mnemonics and learning tricks for causal order are:

- Remember the acronym C.A.U.S.E: Causal order, Affects consistency, Uses logical clocks, Sends messages in order, Enforces happens-before relation.
- Think of a distributed system as a group of people chatting online. Causal order means that if Alice sends a message to Bob and then to Carol, Bob will see Alice's message before Carol's, and Carol will see both messages in the same order as Bob.
- Visualize causal order as a directed acyclic graph (DAG), where each node is an event, and each edge is a message. Causal order means that there is a path from e1 to e2 in the DAG if and only if e1 causally precedes e2.