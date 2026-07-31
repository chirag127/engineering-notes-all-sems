### Timestamp ordering for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Timestamp ordering is a technique for ensuring serializability of transactions in a distributed system.
- A timestamp is a unique identifier assigned to each transaction or event that occurs in the system, based on a logical or physical clock.
- Timestamp ordering defines a partial or total order of transactions or events, according to their timestamps, such that causally related transactions or events have consistent ordering.
- Timestamp ordering can be used to prevent or detect conflicts among concurrent transactions, such as read-write, write-write, or write-read conflicts.
- Timestamp ordering can be implemented using different algorithms, such as Lamport timestamps, vector clocks, or synchronized clocks.
- Lamport timestamps are logical clocks that assign a monotonically increasing number to each event in the system, based on the local clock of the node where the event occurs and the messages received from other nodes.
- Vector clocks are logical clocks that assign a vector of numbers to each event in the system, where each element of the vector represents the local clock of a node in the system, and the vector is updated whenever an event occurs or a message is sent or received.
- Synchronized clocks are physical clocks that are adjusted periodically to maintain a common notion of time among the nodes in the system, using algorithms such as NTP or Cristian's algorithm.