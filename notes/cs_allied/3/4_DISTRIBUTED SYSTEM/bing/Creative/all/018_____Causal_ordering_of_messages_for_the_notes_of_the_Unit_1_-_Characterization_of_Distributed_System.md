# Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj  .
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is useful for ensuring consistency and correctness of distributed applications that depend on the causal relationships between events .
- Causal ordering of messages is not automatically guaranteed in distributed systems, because of transmission delays, network congestion, or different clock rates .
- To achieve causal ordering of messages, various algorithms and protocols have been proposed, such as vector clocks, logical clocks, Lamport timestamps, or causal multicast   .
- These algorithms and protocols use different mechanisms to track and enforce the causal dependencies between messages, such as appending timestamps, piggybacking information, or maintaining buffers   .
- Causal ordering of messages is a weaker form of ordering than total ordering or synchronous ordering, which impose a global order on all messages in the system .
- Causal ordering of messages is also stronger than FIFO ordering or unordered communication, which do not respect the causal dependencies between messages .