### Dynamic voting protocols

- Dynamic voting protocols are a technique for maintaining consistency and availability of replicated data in distributed systems.
- The idea is to assign a number of votes to each replica of a data item, and to require a majority of votes to access or update the data item.
- The number of votes can be dynamically adjusted based on the availability and reliability of the replicas, the network topology, and the access patterns of the data item.
- Dynamic voting protocols can improve the performance and fault tolerance of distributed systems by reducing the communication and synchronization overhead, and by allowing more concurrency and flexibility in accessing the data item.
- Some examples of dynamic voting protocols are:

  - Dynamic weighted voting: A protocol that assigns different weights to different replicas based on their availability and reliability, and requires a weighted majority of votes to access or update the data item  .
  - Topological dynamic voting: A protocol that assigns votes to replicas based on their network proximity and connectivity, and requires a majority of votes within a non-partitionable group of replicas to access or update the data item .
  - Quorum-based voting: A protocol that defines a set of subsets of replicas, called quorums, such that any two quorums have a non-empty intersection, and requires a quorum of votes to access or update the data item.