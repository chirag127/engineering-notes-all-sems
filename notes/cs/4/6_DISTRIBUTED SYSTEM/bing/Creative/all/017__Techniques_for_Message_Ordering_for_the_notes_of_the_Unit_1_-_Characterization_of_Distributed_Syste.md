### Techniques for Message Ordering for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Message ordering is the problem of ensuring that messages sent and received by processes in a distributed system are consistent with some desired order.
- Message ordering is important for applications that require coordination, consistency, or agreement among processes, such as distributed databases, replicated servers, or consensus protocols.
- There are different types of message ordering, depending on the level of synchronization and causality among processes and events.
- An event is an occurrence of sending or receiving a message by a process. Events can be ordered according to the happened-before relation, denoted by `->`, which is defined as follows:
  - If `a` and `b` are events in the same process and `a` occurs before `b`, then `a -> b`.
  - If `a` is the event of sending a message by a process and `b` is the event of receiving that message by another process, then `a -> b`.
  - If `a -> b` and `b -> c`, then `a -> c` (transitivity).
- Two events `a` and `b` are concurrent, denoted by `a || b`, if neither `a -> b` nor `b -> a`.
- The happened-before relation is a partial order, meaning that not all events are comparable. It captures the causal dependencies among events in a distributed system.
- A message ordering technique is a protocol that ensures that messages are delivered to processes in a certain order, according to some criteria. Some common message ordering techniques are :
  - Non-FIFO ordering: This is the simplest and most basic technique, where messages are delivered in any order, regardless of the order of sending. This technique does not guarantee any consistency or synchronization among processes, and may lead to confusion or inconsistency in the application state.
  - FIFO ordering: This technique ensures that messages sent by the same process are delivered in the order of sending. This technique guarantees that the order of events in a single process is preserved, but does not guarantee any causal or logical order among events in different processes.
  - Causal ordering: This technique ensures that messages are delivered in a way that is consistent with the happened-before relation. This technique guarantees that the order of causally dependent events is preserved, but does not guarantee any total or global order among all events in the system.
  - Total ordering: This technique ensures that messages are delivered in the same order to all processes. This technique guarantees that the order of all events is the same for all processes, but does not guarantee any causal or logical order among events.
  - Synchronous ordering: This technique ensures that messages are delivered in a way that is consistent with both the happened-before relation and a global clock. This technique guarantees that the order of all events is the same for all processes, and that the order of events is also consistent with the physical time of occurrence.

- Each message ordering technique has its own advantages and disadvantages, depending on the application requirements and the network characteristics. Some factors that affect the choice of message ordering technique are:
  - Performance: Different techniques may have different overheads in terms of message complexity, latency, or bandwidth. For example, non-FIFO ordering has the lowest overhead, but also the lowest consistency. Total ordering has the highest consistency, but also the highest overhead.
  - Reliability: Different techniques may have different levels of fault tolerance or resilience to node or link failures. For example, non-FIFO ordering is the most robust to failures, but also the most prone to inconsistency. Synchronous ordering is the most sensitive to failures, but also the most accurate in terms of time.
  - Scalability: Different techniques may have different scalability limits or trade-offs in terms of the number of processes, the size of messages, or the frequency of communication. For example, non-FIFO ordering is the most scalable, but also the most unpredictable. Total ordering is the least scalable, but also the most deterministic.

- Some examples of applications that use different message ordering techniques are :
  - Non-FIFO ordering: This technique is suitable for applications that do not require any coordination or consistency among processes, such as peer-to-peer file sharing, online gaming, or streaming media.
  - FIFO ordering: This technique is suitable for applications that require some level of consistency or synchronization among processes, such as distributed logging, chat systems, or bulletin boards.
  - Causal ordering: This technique is suitable for applications that require causal consistency