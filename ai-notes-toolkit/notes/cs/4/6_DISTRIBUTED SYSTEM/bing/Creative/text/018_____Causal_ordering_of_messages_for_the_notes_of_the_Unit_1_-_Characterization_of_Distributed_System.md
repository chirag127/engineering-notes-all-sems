### Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj .
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is based on the concept of potential causality, which is defined by the Lamport's happened-before relation .
- The Lamport's happened-before relation states that if event A happens before event B in the same process, or if event A is the sending of a message and event B is the receipt of that message, then A -> B.
- Causal ordering of messages ensures that if A -> B, then A cannot possibly have caused B, and therefore A and B can be executed concurrently.
- Causal ordering of messages can be implemented by using vector clocks, which are arrays of logical clocks that keep track of the causal dependencies among events in a distributed system .
- Vector clocks can be used to label each message with a vector timestamp that reflects the causal history of the message .
- A process can deliver a message only if its vector timestamp is less than or equal to the current vector clock of the process .
- Causal ordering of messages can be useful for applications that require consistency and concurrency control, such as collaborative editing, distributed databases, and replicated state machines .