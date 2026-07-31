### Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- A distributed system is a collection of independent processes that communicate by exchanging messages over a network.
- Events are occurrences that happen at a specific point in time and space in a distributed system, such as sending or receiving a message, or executing a local operation.
- The order of events is important for understanding the behavior and correctness of a distributed system, especially in the presence of concurrency and failures.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be represented by a directed acyclic graph (DAG), where nodes are events and edges are ordering relations.
- A causal order is a partial order that captures the notion of potential causality between events. An event e1 is causally related to an event e2, denoted by e1 -> e2, if one of the following conditions holds:
  - e1 and e2 are events in the same process, and e1 occurred before e2.
  - e1 is the sending of a message m, and e2 is the receipt of the same message m.
  - There exists an event e3 such that e1 -> e3 and e3 -> e2.
- A total order is a partial order that satisfies an additional property: comparability. This means that for any two events e1 and e2, either e1 -> e2, or e2 -> e1, or both (if e1 and e2 are the same event). A total order can be represented by a linear sequence of events, where each event is preceded by all its causal predecessors and followed by all its causal successors.
- A total causal order is a total order that is consistent with the causal order. This means that if e1 -> e2 in the causal order, then e1 -> e2 in the total order as well. A total causal order is the strictest ordering in distributed systems; it establishes only one linearization, consistent with the causal order, among all the events that occur in the system, even those that occur concurrently .
- A total causal order can be implemented by using a logical clock, such as a vector clock, that assigns a timestamp to each event, such that the timestamp reflects the causal order. A vector clock is an array of integers, one for each process in the system, that is incremented by one when a process executes a local event, and is updated with the maximum of its own and the sender's vector clock when a process receives a message. A vector clock can be used to compare the order of events by using the following rules :
  - If VC(e1) < VC(e2), then e1 -> e2.
  - If VC(e1) > VC(e2), then e2 -> e1.
  - If VC(e1) = VC(e2), then e1 and e2 are the same event.
  - If none of the above holds, then e1 and e2 are concurrent events, denoted by e1 || e2.
- A total causal order can also be achieved by using a total order broadcast, which is a communication primitive that delivers messages to all processes in the same total order, such that the order is consistent with the causal order. A total order broadcast can be implemented by using a sequencer, which is a special process that assigns a sequence number to each message and broadcasts it to all processes. The processes then deliver the messages in the order of the sequence numbers .