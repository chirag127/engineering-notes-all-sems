### Total causal order for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Total causal order is a type of message ordering in distributed systems that ensures that all messages are delivered in the same order to all processes, regardless of their causal relationship or concurrency .
- Total causal order is the strictest ordering in distributed systems; it establishes only one linearization, consistent with the causal ordering, among all the events that occur in the system, even those that occur concurrently.
- Total causal order implies causal order, but not vice versa. Causal order only requires that messages that are causally related (i.e., have a happens-before relationship) are delivered in the same order, but allows concurrent messages (i.e., those that have no causal relationship) to be delivered in different orders to different processes .
- Total causal order can be implemented using different protocols, such as:
  - ISIS system: This system uses vector timestamps and reliable multicast to implement causally ordered multicast between the members of a process group. It also provides other multicast facilities, such as unordered, totally ordered, and sync-ordered multicast.
  - Birman Schipher Stephenson Protocol: This protocol uses a logical clock and a message buffer to ensure that messages are delivered in total causal order. It requires that a message is delivered to a process only if the message immediately preceding it has been delivered to the process. Otherwise, the message is buffered until the preceding message arrives.
  - Schipher Eggli Sandoz Protocol: This protocol is similar to the Birman Schipher Stephenson Protocol, but it uses a vector clock instead of a logical clock. It also requires that a message is delivered to a process only if all the messages that causally precede it have been delivered to the process. Otherwise, the message is buffered until all the preceding messages arrive.
- Total causal order has some advantages and disadvantages, such as:
  - Advantages: It simplifies the design of distributed algorithms that rely on consistent global state, such as distributed debugging, garbage collection, deadlock detection, etc. It also ensures that all processes have a consistent view of the system events and can agree on the outcomes of distributed computations .
  - Disadvantages: It imposes a high overhead on the system performance, as it requires additional messages, timestamps, buffers, and synchronization mechanisms. It also reduces the concurrency and scalability of the system, as it forces all processes to follow the same order of events, even if they are not causally related .
- A possible mnemonic to remember the concept of total causal order is:

  - **T**otal causal order is the **T**oughest ordering in distributed systems
  - It **T**ies all events in one linearization, even if they are **T**emporally concurrent
  - It can be implemented using **T**imestamps, **T**ransmissions, and **T**emporary buffers
  - It has advantages for **T**roubleshooting and **T**erminating distributed algorithms
  - It has disadvantages for **T**hroughput and **T**hriving of distributed systems