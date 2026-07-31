### Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj  .
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is useful for applications that need to preserve the logical dependencies between events in a distributed system .
- Causal ordering of messages is not automatically guaranteed in distributed systems, because of transmission delays, network congestion, or clock synchronization issues .
- To achieve causal ordering of messages, various algorithms have been proposed, such as vector clocks, logical clocks, or piggybacking techniques  .
- These algorithms use timestamps or counters to label the messages and compare them at the receiver side to determine the causal order  .
- Causal ordering of messages is a weaker form of ordering than total ordering or synchronous ordering, but stronger than unordered or FIFO ordering .