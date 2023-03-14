 Here is the content in markdown format for the topic ### Techniques for Message Ordering for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM:

### Techniques for Message Ordering

The following are the techniques used for maintaining message ordering in distributed systems:

1. **Send Sequence Numbers:** Each message is stamped with a sequence number by the sender. The receivers deliver the messages in the same order as indicated by the sequence numbers. This ensures FIFO ordering. However, this technique does not work if sequence numbers are reused or message delays vary significantly.
2. **Logical Clocks:** Each process maintains a logical clock which is incremented whenever it sends a message. The timestamp is attached to the message. The receiver delivers messages in the increasing order of timestamps. This ensures causal ordering but logical clocks can increase out of order.
3. **Vector Clocks:** Each process maintains a vector of logical clocks, one component for each other process. When a message is sent, the vector timestamp is attached to the message and components are incremented. The receiver delivers messages in the increasing timestamp order. This ensures causal ordering and handles out of order increases in logical clocks. However, the size of timestamps increases with the number of processes.
4. **Lamport Timestamps:** Each message is stamped with a timestamp obtained from a global counter. The receiver delivers messages in the increasing timestamp order. This ensures causal ordering but requires synchronization to maintain a global counter.

Advantages and disadvantages of each technique can be discussed in detail. Examples and applications of the techniques can also be included. Mnemonics and learning tricks can be included if easy to remember and helpful for learning. Detailed diagrams can be added to explain the concepts.