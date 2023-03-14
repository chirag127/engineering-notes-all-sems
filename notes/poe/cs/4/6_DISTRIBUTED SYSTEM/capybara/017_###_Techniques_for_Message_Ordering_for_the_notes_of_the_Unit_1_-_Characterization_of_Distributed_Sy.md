### Techniques for Message Ordering for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

Message ordering is an important aspect of distributed systems, as it ensures that messages are delivered and processed in the correct order. In this unit, we will discuss the techniques used for message ordering in distributed systems.

The following are the techniques for message ordering in distributed systems:

1. Total Ordering

Total ordering is a technique in which all messages are delivered in the same order to all processes. It ensures that all processes receive the same message in the same order. This technique is commonly used in distributed systems that require consistency, such as databases.

2. FIFO Ordering

FIFO ordering is a technique in which messages are delivered in the order they are sent. It ensures that messages are delivered to the recipient in the same order they were sent. This technique is commonly used in messaging systems and communication protocols.

3. Casual Ordering

Casual ordering is a technique in which messages are delivered in a causal order. A causal order means that messages are delivered in an order that preserves the causality of events. This technique is commonly used in distributed systems that require event ordering, such as distributed simulations.

4. Lamport Timestamps

Lamport timestamps are a technique used to order events in a distributed system. Each event is assigned a timestamp based on the time it occurred. Lamport timestamps ensure that events are ordered correctly, even if they occur concurrently. This technique is commonly used in distributed systems that require event ordering.

5. Vector Clocks

Vector clocks are a technique used to order events in a distributed system. Each process maintains a vector clock that reflects the order of events it has seen. Vector clocks ensure that events are ordered correctly, even if they occur concurrently. This technique is commonly used in distributed systems that require event ordering.

Mnemonics and Learning tricks:
- Remember the first letter of each technique, i.e., Total, FIFO, Casual, Lamport, and Vector. You can make a phrase using these letters to remember the sequence, such as "The Five CLV Techniques for Message Ordering."
- For Lamport timestamps and Vector clocks, remember that they are both used for event ordering, so you can associate them with the letter "E" in "Event" to remember the order.